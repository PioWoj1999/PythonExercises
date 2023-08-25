from codingbat.List_2.count_evens import count_evens


def test_how_many_evens() -> None:
    assert count_evens([2, 1, 2, 3, 4]) == 3
    assert count_evens([2, 2, 0]) == 3
    assert count_evens([1, 3, 5]) == 0
