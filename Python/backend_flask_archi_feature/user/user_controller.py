from flask import Blueprint, jsonify, request
from flask_expects_json import expects_json
from user.user_module import user_module

user_bp = Blueprint('user', __name__)

user_service = user_module["service"]
user_dto_mapper = user_module["dto_mapper"]
user_dto_schema = user_module["dto_schema"]

@user_bp.route('/users', methods=['GET'])
def list_users():
    users = user_service.list_all_users()
    return jsonify(user_dto_mapper.to_external_list(users)), 200

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user_dto_mapper.to_external(user)), 200
    return jsonify({"error": "User not found"}), 404

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
@expects_json(user_dto_schema)
def update_user(user_id):
    dto = request.json
    updated_user = user_dto_mapper.to_domain(dto, user_id)
    result = user_service.update_user(user_id, updated_user)
    if result:
        return jsonify(user_dto_mapper.to_external(result)), 200
    return jsonify({"error": "User not found"}), 404

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_service.delete_user(user_id)
    return jsonify(), 204