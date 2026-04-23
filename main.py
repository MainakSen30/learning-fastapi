from fastapi import FastAPI, Request
from mockData import products
from dtos import ProductDTO

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
@app.get("/greet")
def greet_user(request: Request):
    query_parameters = (dict(request.query_params))
    print(query_parameters)

    return {
        "greet": f"Hello {query_parameters.get("name")}, how are you",
        "age": f"You are {query_parameters.get("age")} years old"
    }

##ways to send data to server
## body data
## headers (request headers)
## query params

##different types of http methods
@app.post("/create_product")
def create_product(body: ProductDTO):
    product_data = body.model_dump()
    products.append(product_data)
    return {
        "status": "product created successfully.",
        "data": products
    }

## update
@app.put("/update_product/{product_id}")
def update_product(body: ProductDTO, product_id: int):
    for index, p in enumerate(products):
        if p.get("id") == product_id:
            products[index] = body.model_dump()
            return {
                "status": "Product updated successfully...",
                "data": body
            }
    return {
        "status": "Product not found with the given id"
    }


@app.delete("/delete_product/{product_id}")
def delete_product(product_id: int):
    for index, p in enumerate(products):
        if p.get("id") == product_id:
            deleted_product = products.pop(index)
            return {
                "status": "product deleted successfully...",
                "product": deleted_product
            }
    return {
        "status": "Product not found with the given id"
    }
##pydantic
##how to call different http methods - Any TOOL? Postman

##how to validate data - DTOS
