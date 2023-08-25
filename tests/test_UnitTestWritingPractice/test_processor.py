from UnitTestWritingPractice.pay.processor import PaymentProcessor
import pytest

API_KEY = "6cfb67f3-6281-4031-b893-ea85db0dce20"


def test_api_key_invalid() -> None:
    # if not successful, raise error
    with pytest.raises(ValueError):
        processor = PaymentProcessor("")
        processor.charge("1249190007575069", 12, 2024, 100)


def test_card_valid_date() -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge("1249190007575069", 12, 2024, 100)


def test_card_invalid_date() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge("1249190007575069", 12, 1900, 100)


def test_card_number_invalid_luhn() -> None:
    processor = PaymentProcessor("")
    assert not processor.luhn_checksum("1249190007575068")


def test_card_number_valid_luhn() -> None:
    processor = PaymentProcessor("")
    assert processor.luhn_checksum("1249190007575069")


def test_charge_card_invalid() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge(card="1249190007575068", month=12, year=2024, amount=100)


def test_charge_card_valid() -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge(card="1249190007575069", month=12, year=2024, amount=100)
