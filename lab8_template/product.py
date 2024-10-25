from template import Template


class Product(Template):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def message_admin(self, data):
        print(f'Wrong value: {data}')

    def validate_output(self, data):
        if 'price' in data:
            price = data['price'] <= 0
            if price:
                self.message_admin(data)
                return self.response_status(True)

        if 'name' in data:
            wrong_name = type(data['name']) != str or len(data['name']) < 0
            if wrong_name:
                self.message_admin(data)
                return self.response_status(True)

    def before_save_hook(self):
        print(f'Before saving: Product name: {self.name}, product price: {self.price}')

    def after_save_hook(self):
        print(f'After saving: Product name: {self.name}, product price: {self.price}')
