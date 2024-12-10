from flask import Blueprint, jsonify

bp = Blueprint('main', __name__)

@bp.route('/resources', methods=['GET'])
def get_resources():
    resources = [
        {"name": "Resource 1", "description": "Description of Resource 1"},
        {"name": "Resource 2", "description": "Description of Resource 2"}
    ]
    return jsonify(resources)
