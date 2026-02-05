import unittest
from app import create_app
from app.extensions import db
from app.models import Customer
from app.utils.auth import encode_token
from config import TestingConfig


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()

        with self.app.app_context():
            db.drop_all()
            db.create_all()

            self.customer = Customer(
                name="Test User",
                email="tuser@example.com",
                phone="123-123-1234",
                password="password123",
            )
            db.session.add(self.customer)
            db.session.commit()

            self.customer_id = self.customer.id
            self.token = encode_token(self.customer.id)

    # Authorization
    def auth_header(self):
        return {"Authorization": f"Bearer {self.token}"}

    # Create customer
    def test_create_customer(self):
        payload = {
            "name": "New User",
            "email": "new@example.com",
            "password": "password",
            "phone": "123-123-1234"
        }

        response = self.client.post("/customers", json=payload)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["name"], "New User")

    # Create customer (invalid)
    def test_create_invalid(self):
        payload = {
            "name": "Bad Data",
            "password": "password"
        }

        response = self.client.post("/customers", json=payload)

        self.assertEqual(response.status_code, 400)

    # Login
    def test_login(self):
        payload = {
            "email": "tuser@example.com",
            "password": "password123"
        }

        response = self.client.post("/customers/login", json=payload)

        self.assertEqual(response.status_code, 200)
        self.assertIn("auth_token", response.json)

    # Login (invalid)
    def test_login_invalid(self):
        payload = {"email": "invalid@example.com", "password": "invalid"}

        response = self.client.post("/customers/login", json=payload)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json["error"], "Invalid email or password")

    # Get all customers
    def test_get_all_customers(self):
        response = self.client.get("/customers", headers=self.auth_header())

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        self.assertGreaterEqual(len(response.json), 1)

    # Get customer (me)
    def test_get_customer_by_id(self):
        response = self.client.get("/customers/me", headers=self.auth_header())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["email"], "tuser@example.com")

    # Get customer (unauthorized / missing token)
    def test_get_customer_invalid(self):
        response = self.client.get("/customers/me")

        self.assertEqual(response.status_code, 401)
        self.assertIn("error", response.json)

    # Update customer
    def test_update_customer(self):
        payload = {"name": "Updated Name"}

        response = self.client.put(
            "/customers/me",
            json=payload,
            headers=self.auth_header()
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], "Updated Name")

    # Update customer (invalid)
    def test_update_customer_invalid(self):
        payload = {"email": "not-an-email"}

        response = self.client.put(
            "/customers/me",
            json=payload,
            headers=self.auth_header()
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("email", response.json)

    # Delete customer
    def test_delete_customer(self):
        response = self.client.delete("/customers/me", headers=self.auth_header())

        self.assertEqual(response.status_code, 200)
        self.assertIn("successfully deleted", response.json["message"])

    # Delete customer (unauthorized / missing token)
    def test_delete_customer_invalid(self):
        response = self.client.delete("/customers/me")

        self.assertEqual(response.status_code, 401)
        self.assertIn("error", response.json)


if __name__ == "__main__":
    unittest.main()