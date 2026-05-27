from flask import Blueprint, jsonify

bp = Blueprint("products", __name__, url_prefix="/products")


@bp.route("/")
def products():
    message = '----- Flask Rest | Products -----'
    # return jsonify([])
    return jsonify(message)
