from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Hello, World!"

    return app

def start_flask_app():
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)  # Use 0.0.0.0 to allow external access

if __name__ == "__main__":
    start_flask_app()
