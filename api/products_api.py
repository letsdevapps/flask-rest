from flask import Blueprint, jsonify

from service import product_service

bp = Blueprint("products_api", __name__, url_prefix="/api/products")

@bp.route("/", methods=["GET"])
def products():
    message = '----- Flask Rest | Products -----'
    # return jsonify([])
    return jsonify(message)

@bp.route("/index")
def index():
    return jsonify(product_service.index())