# This is the entry point of the application. Run this file to start the Flask app.
# It imports the app from app.py and launches the development server.

from app import app

if __name__ == "__main__":
    app.run(debug=True)