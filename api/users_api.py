from flask import Blueprint, jsonify

bp = Blueprint("users_api", __name__, url_prefix="/api/users")

@bp.route("/", methods=["GET"])
def users():
    message = '----- Flask Rest | Users -----'
    #return jsonify([])
    return jsonify(message)
