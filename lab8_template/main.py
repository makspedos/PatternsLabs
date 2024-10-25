from lab8_template.order import Order
from product import Product
from user import User

if __name__ == '__main__':
    product = Product(name='Bread', price=25)
    product_update = {
        "price": -1,
    }
    print(product.template_method(data=product_update))

    user = User(username='test', password='testuser123', email='test@gmail.com')
    user_update = {
        "username": 'test123',
        "email": "test123@gmail.com",
    }
    print(user.template_method(data=user_update))

    order = Order(id = 1, user=user, product=product)
    json, status = order.template_method(data=user_update)
    print(json)
    print(status)
