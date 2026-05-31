from flask import Flask

from api.products_api import bp as products_api
from api.users_api import bp as users_api
from consume.products_consume import bp as products_consume
from web.product_web import product_web

app = Flask(__name__)
app.register_blueprint(users_api)
app.register_blueprint(products_api)
app.register_blueprint(products_consume)
app.register_blueprint(product_web)


@app.route('/')
def root():
    return '----- Flask Rest | Root -----'


if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0", port=5000, debug=True)
