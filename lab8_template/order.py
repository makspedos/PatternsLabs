from template import Template
from user import User
from product import Product

class Order(Template):
    def __init__(self, id:int, user:User, product:Product):
        self.id = id
        self.user = user
        self.product = product

    def response_status(self, code=None):
        json_data = {
            "id": self.id,
            "user": {
                "username": self.user.username,
                "email": self.user.email,
            },
            "product": {
                "name": self.product.name,
                "price": self.product.price,
            }
        }
        status_code = super().response_status()
        return json_data, status_code