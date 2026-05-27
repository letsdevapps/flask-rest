from flask import Blueprint, jsonify

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("/")
def users():
    message = '----- Flask Rest | Users -----'
    #return jsonify([])
    return jsonify(message)
