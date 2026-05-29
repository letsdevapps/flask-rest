from flask import Blueprint, render_template

product_web = Blueprint("product_web", __name__, url_prefix="/products")

@product_web.route("/")
def page():
    products = ["Camiseta", "Notebook", "Mouse"]
    return render_template("products.html", products=products)