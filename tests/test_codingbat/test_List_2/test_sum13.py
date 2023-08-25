from codingbat.List_2.sum13 import sum13


def test_sum13() -> None:
    assert sum13([1, 2, 2, 1]) == 6
    assert sum13([1, 1, 13, 2, 1]) == 3
    assert sum13([1, 2, 2, 1, 13]) == 6
    assert sum13([13, 1, 2, 13, 2, 1, 13]) == 3
