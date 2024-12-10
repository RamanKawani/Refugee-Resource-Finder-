# flask_app.py

from flask import Flask

def create_app():
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__)

    # Define routes here
    @app.route('/')
    def home():
        return "Hello, World! Welcome to the Refugee Resource Finder."

    @app.route('/about')
    def about():
        return "This app helps refugees find resources in their area."

    return app
