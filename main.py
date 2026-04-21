from fastapi import FastAPI
from mockData import products

app = FastAPI()

@app.get("/")
def home() :
    return "Welcome to FastAPI series!"

@app.get("/products")
def get_products():
    return products

#path params
@app.get("/product/{product_id}")
def get_one_product(product_id: int):
    ##if product is available with the given id, return the product details, else return error message
    product = None
    for p in products:
        if p.get("id") == product_id:
            return p
    return {
        "error": "Product not found with the given id"
    }

##query params
