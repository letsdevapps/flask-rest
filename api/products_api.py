from flask import Blueprint, jsonify, request

from service import product_service

bp = Blueprint("products_api", __name__, url_prefix="/api/products")


@bp.route("")
@bp.route("/")
@bp.route("/index", methods=["GET"])
def get_products():
    message = '----- Flask Rest | Products -----'
    # return jsonify(message)
    return jsonify(product_service.index())


@bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = product_service.show(product_id)
    if product:
        return jsonify(product)
    return jsonify({"error": "Produto não encontrado"}), 404


@bp.route("/", methods=["POST"])
def create_product():
    data = request.json
    if "name" not in data:
        return jsonify({"error": "Campo 'name' é obrigatório"}), 400
    product = product_service.create(data["name"])
    return jsonify(product), 201


@bp.route("/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.json
    if "name" not in data:
        return jsonify({"error": "Campo 'name' é obrigatório"}), 400
    product = product_service.update(product_id, data["name"])
    if product:
        return jsonify(product)
    return jsonify({"error": "Produto não encontrado"}), 404


@bp.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    if product_service.delete(product_id):
        return jsonify({"message": "Produto deletado com sucesso"})
    return jsonify({"error": "Produto não encontrado"}), 404
