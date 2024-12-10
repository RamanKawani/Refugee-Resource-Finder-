from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register routes (views)
    from . import views
    app.register_blueprint(views.bp)

    return app
