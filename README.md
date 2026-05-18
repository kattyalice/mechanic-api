# 🔧 Mechanic Shop API

Production-style REST API for managing customers, mechanics, inventory, and service tickets. Built with Flask, SQLAlchemy, JWT authentication, Swagger docs, and deployed on Render.

Live Swagger Docs: https://mechanic-api-kattyalice-3sbu.onrender.com/

⸻

## 🚀 Stack
	•	Python
	•	Flask
	•	SQLAlchemy ORM
	•	Marshmallow validation
	•	JWT authentication (Bearer tokens)
	•	Swagger / OpenAPI docs
	•	PostgreSQL
	•	Gunicorn
	•	Render deployment
	•	GitHub CI/CD workflow

⸻

## ✨ Core Features

### Customers
	•	Register and login
	•	JWT token generation
	•	Protected update/delete routes
	•	Self-service customer endpoints

### Mechanics
	•	Full CRUD operations
	•	Pagination support
	•	Most-active mechanic endpoint

### Inventory
	•	CRUD operations
	•	Protected routes
	•	Pagination support

### Service Tickets
	•	Create service tickets
	•	Assign and remove mechanics
	•	Add inventory parts to tickets
	•	Logged-in customer ticket lookup

⸻

## 🔐 Authentication

Login endpoint:

POST /customers/login

Use returned token in protected routes:

Authorization: Bearer <your_token>

Swagger UI includes built-in Authorize support.

⸻

## 🧪 Testing

Includes automated tests for:
	•	Authentication
	•	Protected routes
	•	CRUD endpoints
	•	Ticket and inventory flows

## Run locally:

python -m unittest discover -s tests

⸻

## ⚙️ Run Locally

Clone repo and install dependencies:

git clone 
pip install -r requirements.txt
flask run

Required environment variables:

SECRET_KEY
DATABASE_URL

⸻

## 📘 API Docs

Test endpoints directly in the browser with JWT auth.

⸻

## 👩‍💻 Author

Kathryn Baldridge
Backend / Full-Stack Developer
https://github.com/kattyalice
