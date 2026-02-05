from datetime import datetime, timedelta
from jose import jwt
from flask import current_app, request, jsonify, g
from functools import wraps
import os

SECRET_KEY = os.environ.get('SECRET_KEY') or "super secret secrets"

def _get_secret_key():
    return str(current_app.config.get("SECRET_KEY")or os.environ.get("SECRET_KEY") or SECRET_KEY)

def encode_token(customer_id):
    payload = {
        "customer_id": customer_id,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }

    return jwt.encode(
        payload,
        _get_secret_key(),
        algorithm="HS256"
    )

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"error": "Authorization header missing"}), 401

        parts = auth_header.split()

        if len(parts) != 2 or parts[0].lower() != "bearer":
            return jsonify({"error": "Invalid token format"}), 401

        token = parts[1]

        try:
            data = jwt.decode(
                token,
                _get_secret_key(),
                algorithms=["HS256"]
            )
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.JWTError:
            return jsonify({"error": "Invalid token"}), 401

        customer_id = data.get("customer_id")
        if not customer_id:
            return jsonify({"error": "Invalid token payload"}), 401
            
        g.customer_id = customer_id

        return f(*args, **kwargs)

    return decorated