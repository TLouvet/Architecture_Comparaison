from flask import Blueprint, jsonify, request
from flask_expects_json import expects_json
from author.author_module import author_module

author_bp = Blueprint('author', __name__)

author_service = author_module["service"]
author_mapper = author_module["dto_mapper"]
author_dto_schema = author_module["dto_schema"]

@author_bp.route('/authors', methods=['GET'])
def list_authors():
    authors = author_service.list_all_authors()
    return jsonify(author_mapper.to_external_list(authors)), 200

@author_bp.route('/authors/<int:author_id>', methods=['GET'])
def get_author(author_id):
    author = author_service.get_author_by_id(author_id)
    if author:
        return jsonify(author_mapper.to_external(author)), 200
    return jsonify({"error": "Author not found"}), 404

@author_bp.route('/authors', methods=['POST'])
@expects_json(author_dto_schema)
def create_author():
    dto = request.json
    author = author_mapper.to_domain(dto)
    created_author = author_service.create_author(author)
    return jsonify(author_mapper.to_external(created_author)), 201

@author_bp.route('/authors/<int:author_id>', methods=['PUT'])
@expects_json(author_dto_schema)
def update_author(author_id):
    dto = request.json
    updated_author = author_mapper.to_domain(dto, author_id)
    result = author_service.update_author(author_id, updated_author)
    if result:
        return jsonify(author_mapper.to_external(result)), 200
    return jsonify({"error": "Author not found"}), 404

@author_bp.route('/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id):
    author_service.delete_author(author_id)
    return jsonify(), 204
