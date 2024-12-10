from flask import jsonify, request
from extensions import db
from models import Resource

def init_routes(app):
    @app.route('/resources', methods=['GET'])
    def get_resources():
        resources = Resource.query.all()
        return jsonify([resource.to_dict() for resource in resources])

    @app.route('/resources', methods=['POST'])
    def add_resource():
        data = request.json
        new_resource = Resource(name=data['name'], description=data['description'])
        db.session.add(new_resource)
        db.session.commit()
        return jsonify(new_resource.to_dict()), 201

