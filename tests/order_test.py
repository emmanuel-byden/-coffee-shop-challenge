import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")
        self.order = Order(self.customer, self.coffee, 5.0)

    def test_price_validation(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 11.0)
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, "5.0")

    def test_price_immutable(self):
        with self.assertRaises(AttributeError):
            self.order.price = 6.0

    def test_customer(self):
        self.assertEqual(self.order.customer.name, "Alice")

    def test_coffee(self):
        self.assertEqual(self.order.coffee.name, "Latte")

if __name__ == '__main__':
    unittest.main()
