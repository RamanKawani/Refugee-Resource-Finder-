# flask_app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

def start_flask_app():
    app.run(debug=True, host='0.0.0.0', port=5000)
