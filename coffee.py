class Coffee:
    _all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters")
        self._name = name
        Coffee._all.append(self)

    @property
    def name(self):
        return self._name

    def orders(self):
        from order import Order
        return [order for order in Order._all if order.coffee == self]

    def customers(self):
        from order import Order
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        return sum(order.price for order in orders) / len(orders) if orders else 0
