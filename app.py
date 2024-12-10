from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Load configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resources.db'  # Replace with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Enable CORS
CORS(app)

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Import routes
from routes import init_routes
init_routes(app)

# Main entry point
if __name__ == '__main__':
    db.create_all()  # Create tables (for development only)
    app.run(debug=True)
