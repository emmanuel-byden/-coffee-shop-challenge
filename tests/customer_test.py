import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")
        self.order = Order(self.customer, self.coffee, 5.0)

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")
        with self.assertRaises(ValueError):
            Customer("A" * 16)
        with self.assertRaises(ValueError):
            Customer(123)

    def test_name_setter(self):
        self.customer.name = "Bob"
        self.assertEqual(self.customer.name, "Bob")
        with self.assertRaises(ValueError):
            self.customer.name = "A" * 16

    def test_orders(self):
        self.assertEqual(len(self.customer.orders()), 1)
        self.assertEqual(self.customer.orders()[0].price, 5.0)

    def test_coffees(self):
        self.assertEqual(len(self.customer.coffees()), 1)
        self.assertEqual(self.customer.coffees()[0].name, "Latte")

    def test_create_order(self):
        new_order = self.customer.create_order(self.coffee, 6.0)
        self.assertEqual(len(self.customer.orders()), 2)
        self.assertEqual(new_order.price, 6.0)

    def test_most_aficionado(self):
        customer2 = Customer("Bob")
        Order(customer2, self.coffee, 10.0)
        aficionado = Customer.most_aficionado(self.coffee)
        self.assertEqual(aficionado.name, "Bob")

if __name__ == '__main__':
    unittest.main()
