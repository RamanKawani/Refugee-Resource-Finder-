from flask import jsonify, request
from app import db
from models import Resource

def init_routes(app):
    @app.route('/resources', methods=['GET'])
    def get_resources():
        resources = Resource.query.all()
        result = [
            {
                'id': resource.id,
                'name': resource.name,
                'type': resource.type,
                'address': resource.address,
                'phone': resource.phone,
                'hours': resource.hours,
                'latitude': resource.latitude,
                'longitude': resource.longitude,
                'description': resource.description,
            }
            for resource in resources
        ]
        return jsonify(result), 200

    @app.route('/resources/<int:id>', methods=['GET'])
    def get_resource(id):
        resource = Resource.query.get_or_404(id)
        return jsonify({
            'id': resource.id,
            'name': resource.name,
            'type': resource.type,
            'address': resource.address,
            'phone': resource.phone,
            'hours': resource.hours,
            'latitude': resource.latitude,
            'longitude': resource.longitude,
            'description': resource.description,
        }), 200

    @app.route('/resources', methods=['POST'])
    def add_resource():
        data = request.json
        new_resource = Resource(
            name=data['name'],
            type=data['type'],
            address=data['address'],
            phone=data.get('phone'),
            hours=data.get('hours'),
            latitude=data['latitude'],
            longitude=data['longitude'],
            description=data.get('description'),
        )
        db.session.add(new_resource)
        db.session.commit()
        return jsonify({'message': 'Resource added successfully!'}), 201

    @app.route('/resources/<int:id>', methods=['PUT'])
    def update_resource(id):
        resource = Resource.query.get_or_404(id)
        data = request.json
        resource.name = data['name']
        resource.type = data['type']
        resource.address = data['address']
        resource.phone = data.get('phone')
        resource.hours = data.get('hours')
        resource.latitude = data['latitude']
        resource.longitude = data['longitude']
        resource.description = data.get('description')
        db.session.commit()
        return jsonify({'message': 'Resource updated successfully!'}), 200

    @app.route('/resources/<int:id>', methods=['DELETE'])
    def delete_resource(id):
        resource = Resource.query.get_or_404(id)
        db.session.delete(resource)
        db.session.commit()
        return jsonify({'message': 'Resource deleted successfully!'}), 200
