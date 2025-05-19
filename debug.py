from customer import Customer
from coffee import Coffee
from order import Order

# Sample usage for testing
if __name__ == "__main__":
    # Create customers
    alice = Customer("Alice")
    bob = Customer("Bob")

    # Create coffees
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")

    # Create orders
    order1 = alice.create_order(latte, 5.0)
    order2 = alice.create_order(espresso, 3.5)
    order3 = bob.create_order(latte, 6.0)

    # Test relationships
    print(f"Alice's orders: {len(alice.orders())}")
    print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")
    print(f"Latte's customers: {[customer.name for customer in latte.customers()]}")
    print(f"Latte's number of orders: {latte.num_orders()}")
    print(f"Latte's average price: {latte.average_price()}")

    # Test bonus
    most_aficionado = Customer.most_aficionado(latte)
    print(f"Most aficionado for Latte: {most_aficionado.name if most_aficionado else None}")
