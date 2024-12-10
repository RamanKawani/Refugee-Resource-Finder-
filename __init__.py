from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import routes and register blueprints
    from . import views
    app.register_blueprint(views.bp)

    return app
