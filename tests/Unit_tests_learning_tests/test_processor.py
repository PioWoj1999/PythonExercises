from Unit_tests_learning.pay.processor import PaymentProcessor
import pytest
from dotenv import load_dotenv
import os

# importing api key from env file
load_dotenv()
API_KEY = os.getenv("API_KEY") or ""


def test_api_key_invalid() -> None:
    #! added if we are expecting the value error
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
