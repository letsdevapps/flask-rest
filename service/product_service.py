from model.product import Product
from dataclasses import asdict

# Banco de dados em memoria
products_db = [
    Product(1, "Camiseta"),
    Product(2, "Notebook"),
    Product(3, "Mouse")
]

# Gerador de ID automatico
def next_id():
    if products_db:
        return max(p.id for p in products_db) + 1
    return 1

def index():
    message = '----- Flask Rest | Product Service | Index -----'
    #return message
    return [asdict(p) for p in products_db]

def show(product_id: int):
    for p in products_db:
        if p.id == product_id:
            return asdict(p)
    return None

def create(name: str):
    new_product = Product(id=next_id(), name=name)
    products_db.append(new_product)
    return asdict(new_product)

def update(product_id: int, name: str):
    for p in products_db:
        if p.id == product_id:
            p.name = name
            return asdict(p)
    return None

def delete(product_id: int):
    global products_db
    for p in products_db:
        if p.id == product_id:
            products_db = [prod for prod in products_db if prod.id != product_id]
            return True
    return False