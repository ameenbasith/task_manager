from flask import Flask, render_template
from routes import user_routes
from models import db

app = Flask(__name__)

app.config.from_object('config')

# Register the user_routes blueprint with the app.
app.register_blueprint(user_routes)

db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
