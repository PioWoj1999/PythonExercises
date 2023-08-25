from pay.order import LineItem, Order
from pay.payment import pay_order


def main():
    # Test card number: 1249190007575069
    # create the order
    order = Order()
    # add elements to order
    order.line_items.append(LineItem(name="Shoes", price=100_00, quantity=2))
    order.line_items.append(LineItem(name="Hat", price=50_00))
    # make the order payment
    pay_order(order)


if __name__ == "__main__":
    main()
