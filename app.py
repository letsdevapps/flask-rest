from flask import Flask
from templates.users import bp as users_bp
from templates.products import bp as products_bp

app = Flask(__name__)
app.register_blueprint(users_bp)
app.register_blueprint(products_bp)


@app.route('/')
def root():
    return '----- Flask Rest | Root -----'


if __name__ == '__main__':
    app.run()
