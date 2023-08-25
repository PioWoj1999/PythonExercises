from codingbat.String_2.count_hi import count_hi


def test_count_hi() -> None:
    assert count_hi("hihi") == 2
    assert count_hi("abc hi ho") == 1
    assert count_hi("ABCh hi i") == 1
