from database.db import db
from src.models.entities import Product
from typing import List


class ProductRepo:
    def create(self, product):
        print(type(product))
        db.session.add(product)
        db.session.commit()

    def fetchById(self, _id) -> 'Product':
        return db.session.query(Product).filter_by(id=_id).first()

    def fetchAll(self) -> List['Product']:
        return db.session.query(Product).all()

    def delete(self, _id) -> None:
        product = db.session.query(Product).filter_by(id=_id).first()
        db.session.delete(product)
        db.session.commit()

    def update(self, product_data):
        db.session.merge(product_data)
        db.session.commit()
