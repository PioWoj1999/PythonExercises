from pay.order import Order, LineItem, OrderStatus


def test_empty_order_total() -> None:
    order = Order()
    assert order.total == 0


def test_order_total() -> None:
    order = Order()
    order.line_items.append(LineItem(name="Test", price=100))
    assert order.total == 100


def test_order_total_2() -> None:
    order = Order()
    order.line_items.append(LineItem(name="Test", price=100))
    order.line_items.append(LineItem(name="Test_2", price=100))
    assert order.total == 200


def test_order_pay() -> None:
    order = Order()
    order.pay()
    assert order.status == OrderStatus.PAID
