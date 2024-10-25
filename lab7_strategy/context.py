from strategy import Strategy


class Context:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def calculate_price(self, distance: int = 0):
        return self.strategy.delivery_cost(distance)
