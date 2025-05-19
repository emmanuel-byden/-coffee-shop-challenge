class Order:
    _all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(price, float):
            raise ValueError("Price must be a float")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order._all.append(self)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        from customer import Customer
        if not isinstance(self._customer, Customer):
            raise ValueError("Customer must be a Customer instance")
        return self._customer

    @property
    def coffee(self):
        from coffee import Coffee
        if not isinstance(self._coffee, Coffee):
            raise ValueError("Coffee must be a Coffee instance")
        return self._coffee
