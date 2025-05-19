class Customer:
    _all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not 1 <= len(name) <= 15:
            raise ValueError("Name must be 1–15 characters")
        self._name = name
        Customer._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be 1–15 characters")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order._all if order.customer == self]

    def coffees(self):
        from order import Order
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        if not coffee.orders():
            return None
        customer_spending = {}
        for order in coffee.orders():
            customer = order.customer
            customer_spending[customer] = customer_spending.get(customer, 0) + order.price
        return max(customer_spending.items(), key=lambda x: x[1])[0]
