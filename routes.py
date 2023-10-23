from flask import Blueprint, request, jsonify, current_app
import jwt
from models import User

user_routes = Blueprint('user_routes', __name__)

@user_routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # Access the app instance from the current application context.
    app = current_app

    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"message": "User already exists"}), 400

    new_user = User(email=email, password=password)
    app.db.session.add(new_user)
    app.db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@user_routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # Access the app instance from the current application context.
    app = current_app

    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        token = jwt.encode({"email": email}, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({"token": token})
    return jsonify({"message": "Invalid credentials"}), 401
