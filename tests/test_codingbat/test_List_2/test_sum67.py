from codingbat.List_2.sum67 import sum67


def test_remove67() -> None:
    assert sum67([1, 2, 2, 6, 99, 99, 7]) == 5
    assert sum67([1, 2, 2, 6, 100, 99, 99, 7]) == 5
