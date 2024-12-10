from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

def start_flask_app():
    # Start the Flask app using Waitress
    serve(app, host='0.0.0.0', port=5000)

