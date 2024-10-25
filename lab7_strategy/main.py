from context import Context
from delivery import SelfPickUp, CompanyCourier, MyCourier

if __name__ == '__main__':
    context = Context(strategy=SelfPickUp())
    print(f'Самовивіз: {context.calculate_price()}')
    context.set_strategy(strategy=CompanyCourier())
    print(f"Кур'єр компанії: {context.calculate_price(distance=2)}")
    context.set_strategy(strategy=MyCourier())
    print(f"Власний кур'єр : {context.calculate_price(distance=2)}")