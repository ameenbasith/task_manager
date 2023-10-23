# app.py - Main application file

from flask import Flask
from routes import user_routes
from models import db

app = Flask(__name__)

app.config.from_object('config')
app.register_blueprint(user_routes)

db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
