from flask import Blueprint, request, jsonify, current_app, render_template
import jwt
from models import User

user_routes = Blueprint('user_routes', __name__)

@user_routes.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.form
        email = data.get("email")
        password = data.get("password")

        app = current_app

        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify({"message": "User already exists"}), 400

        new_user = User(email=email, password=password)
        app.db.session.add(new_user)
        app.db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201
    else:
        # Render the HTML template for registration.
        return render_template("register.html")
