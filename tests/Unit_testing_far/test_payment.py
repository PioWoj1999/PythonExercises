from pay.order import Order, LineItem
from pay.payment import pay_order
from pytest import MonkeyPatch  # to create input from user, class overrides the input
from pay.processor import PaymentProcessor


def test_pay_order(monkeypatch: MonkeyPatch) -> None:
    def charge_mock(
        self: PaymentProcessor, card: str, month: int, year: int, amount: int
    ) -> None:
        pass

    input = ["1249190007575069", "12", "2024"]
    # take by poping from list each element as "user" input
    # lambda is just repeating the process
    monkeypatch.setattr("builtins.input", lambda _: input.pop(0))
    monkeypatch.setattr(PaymentProcessor, "_check_api_key", lambda _: True)
    monkeypatch.setattr(PaymentProcessor, "charge", charge_mock)
    order = Order()
    order.line_items.append(LineItem("Test", 100))
    pay_order(order)
