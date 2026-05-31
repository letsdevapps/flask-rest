import requests
from flask import Blueprint

bp = Blueprint("products_consume", __name__, url_prefix="/consume/products")

BASE_URL = "http://localhost:5000/api/products"


@bp.route("")
def get_products():
    response = requests.get(BASE_URL + "/")
    return response.json()


@bp.route("/<int:product_id>")
def get_product(product_id):
    response = requests.get(f"{BASE_URL}/{product_id}")
    return response.json()


@bp.route("/create/<name>")
def create_product(name):
    payload = {"name": name}
    response = requests.post(BASE_URL + "/", json=payload)
    return response.json()


@bp.route("/update/<product_id>/<name>")
def update_product(product_id, name):
    payload = {"name": name}
    response = requests.put(f"{BASE_URL}/{product_id}", json=payload)
    return response.json()


@bp.route("/delete/<product_id>")
def delete_product(product_id):
    response = requests.delete(f"{BASE_URL}/{product_id}")
    return response.json()

# if __name__ == "__main__":
#     print("LISTANDO:")
#     print(get_products())
#
#     print("\nCRIANDO:")
#     created = create_product("Teclado")
#     print(created)
#
#     new_id = created["id"]
#
#     print("\nBUSCANDO:")
#     print(get_product(new_id))
#
#     print("\nATUALIZANDO:")
#     print(update_product(new_id, "Teclado Mecânico"))
#
#     print("\nDELETANDO:")
#     print(delete_product(new_id))
#
#     print("\nFINAL:")
#     print(get_products())
