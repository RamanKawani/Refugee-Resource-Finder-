# app.py

import os
from flask_app import create_app
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Set up the environment
FLASK_ENV = os.getenv('FLASK_ENV', 'development')

# Create the Flask app
app = create_app()

# Configure app settings based on the environment
if FLASK_ENV == 'development':
    app.config['DEBUG'] = True
    app.config['ENV'] = 'development'
else:
    app.config['DEBUG'] = False
    app.config['ENV'] = 'production'

# Running the app with additional features like logging
if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=int(os.getenv('FLASK_PORT', 5000)))
