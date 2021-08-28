from database.db import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    price = db.Column(db.Float(precision=2), nullable=False)

    def __str__(self):
        return 'ProductModel(id=%d,name=%s, price=%s,)' % (self.id, self.name, self.price)

    def json(self):
        return {'id': self.id, 'name': self.name, 'price': self.price}
