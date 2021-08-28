
from src.models.repositories import ProductRepo
from src.schemas.schemas import ProductSchema
from flask import request

productRepo = ProductRepo()
productSchema = ProductSchema()
productListSchema = ProductSchema(many=True)
PRODUCT_NOT_FOUND = "Product not found for id: {}"


def get(id):
    product_data = productRepo.fetchById(id)
    if product_data:
        return productSchema.dump(product_data)
    return {'message': PRODUCT_NOT_FOUND.format(id)}, 404


def update(id):
    product_data = productRepo.fetchById(id)
    product_req_json = request.get_json()
    if product_data:
        product_data.name = product_req_json['name']
        product_data.price = product_req_json['price']
        productRepo.update(product_data)
        return productSchema.dump(product_data)
    return {'message': PRODUCT_NOT_FOUND.format(id)}, 404


def delete(id):
    product_data = productRepo.fetchById(id)
    if product_data:
        productRepo.delete(id)
        return {'message': 'Product deleted successfully'}, 200
    return {'message': PRODUCT_NOT_FOUND.format(id)}, 404


def create():
    product_req_json = request.get_json()
    product_data = productSchema.load(product_req_json)
    productRepo.create(product_data)
    return productSchema.dump(product_data), 201


def getAll():
    return productListSchema.dump(productRepo.fetchAll()), 200
