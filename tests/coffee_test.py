import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")
        self.order = Order(self.customer, self.coffee, 5.0)

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("Ab")
        with self.assertRaises(ValueError):
            Coffee(123)

    def test_name_immutable(self):
        with self.assertRaises(AttributeError):
            self.coffee.name = "Espresso"

    def test_orders(self):
        self.assertEqual(len(self.coffee.orders()), 1)
        self.assertEqual(self.coffee.orders()[0].price, 5.0)

    def test_customers(self):
        self.assertEqual(len(self.coffee.customers()), 1)
        self.assertEqual(self.coffee.customers()[0].name, "Alice")

    def test_num_orders(self):
        self.assertEqual(self.coffee.num_orders(), 1)
        Order(self.customer, self.coffee, 6.0)
        self.assertEqual(self.coffee.num_orders(), 2)

    def test_average_price(self):
        self.assertEqual(self.coffee.average_price(), 5.0)
        Order(self.customer, self.coffee, 7.0)
        self.assertEqual(self.coffee.average_price(), 6.0)

if __name__ == '__main__':
    unittest.main()
