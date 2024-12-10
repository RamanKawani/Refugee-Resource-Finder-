from flask import Blueprint, jsonify

bp = Blueprint('views', __name__)

@bp.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

@bp.route('/hello')
def hello():
    return jsonify({"message": "Hello, Flask!"})
