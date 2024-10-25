from strategy import Strategy


class SelfPickUp(Strategy):
    def delivery_cost(self, distance:int) ->int:
        return 0


class CompanyCourier(Strategy):
    def delivery_cost(self, distance:int)->int:
        return 5 * distance


class MyCourier(Strategy):
    def delivery_cost(self, distance:int)->int:
        base_fee = 10
        return base_fee + 5 * distance