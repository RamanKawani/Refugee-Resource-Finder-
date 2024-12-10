import streamlit as st
from flask import Flask
from urllib.parse import quote  # Replacing url_quote with quote from urllib.parse
from dotenv import load_dotenv
from waitress import serve  # Import waitress

# Load environment variables from a .env file
load_dotenv()

# Initialize Flask app
def create_app():
    app = Flask(__name__)

    # Sample route using quote function for URL encoding
    @app.route('/')
    def index():
        example_string = "hello world"
        encoded_string = quote(example_string)  # Using urllib.parse.quote
        return f"Encoded string: {encoded_string}"

    return app

# Initialize the app
app = create_app()

# If you want to use waitress to serve the Flask app
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)  # Use waitress to serve the app
