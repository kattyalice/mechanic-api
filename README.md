# 🔧 Mechanic Shop API

Production-style REST API for managing customers, mechanics, inventory, and service tickets. Built with Flask, SQLAlchemy, and JWT authentication, documented with Swagger, and deployed on Render with a Neon PostgreSQL database.

**Live Swagger Docs:** https://mechanic-api-kattyalice-3sbu.onrender.com/

> Hosted on free tiers: the first request after a period of inactivity can take up to a minute while the server wakes up.

---

## 🚀 Stack

- Python / Flask
- SQLAlchemy ORM
- Marshmallow validation
- JWT authentication (Bearer tokens)
- Werkzeug password hashing
- Flask-Limiter rate limiting and Flask-Caching
- Swagger / OpenAPI docs
- PostgreSQL (Neon) in production, SQLite for local development
- Gunicorn
- Render deployment
- GitHub Actions CI/CD workflow

---

## Core Features

### Customers
- Register and log in
- JWT token generation
- Protected update and delete routes
- Self-service customer endpoints (`/customers/me`)

### Mechanics
- Full CRUD operations
- Pagination support
- Most-active mechanic endpoint

### Inventory
- CRUD operations
- Protected routes
- Pagination support

### Service Tickets
- Create service tickets
- Assign and remove mechanics
- Add inventory parts to tickets
- Logged-in customer ticket lookup

---

## 🔐 Security

- Passwords are hashed with Werkzeug before they're stored, never saved as plain text
- Passwords are write-only in the API: accepted on register and update, never returned in responses
- JWT-protected routes for customer data, mechanics, inventory, and tickets
- Rate limiting on endpoints
- Database connections are checked before use, so the app recovers cleanly when the serverless database wakes from idle

---

## 🔑 Authentication

Log in to get a token:

```
POST /customers/login
```
```

Send the token with protected requests:
Send the token with protected requests:

```
```
Authorization: Bearer <your_token>
```

In Swagger, click **Authorize** and enter `Bearer <your_token>`.

---

## ⚙️ Run Locally

Locally, the app runs with `DevelopmentConfig` and a SQLite database, so no external database is needed.

```bash
git clone https://github.com/kattyalice/mechanic-api.git
cd mechanic-api
python -m venv venv
```

Activate the virtual environment:

```bash
# Windows (PowerShell)
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

Install dependencies and start the server:

```bash
pip install -r requirements.txt
python flask_app.py
```

Open http://127.0.0.1:5000 to view the Swagger docs. Set the **Schemes** dropdown to **HTTP** when testing locally.

### Environment Variables

| Variable | Where | Purpose |
| --- | --- | --- |
| `FLASK_CONFIG` | Production | Set to `ProductionConfig` (defaults to `DevelopmentConfig`) |
| `SQLALCHEMY_DATABASE_URI` | Production | PostgreSQL connection string |
| `SECRET_KEY` | Production and local | Signs JWT tokens |

---

## 🧪 Testing

Automated tests cover:
- Authentication
- Protected routes
- CRUD endpoints
- Ticket and inventory flows

Run them locally:

```bash
python -m unittest discover -s tests
```

Tests also run automatically through GitHub Actions on every push.

---

## Author

**Kathryn Baldridge**
Backend / Full-Stack Developer
https://github.com/kattyalice
