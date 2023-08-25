from codingbat.String_2.end_other import end_other


def test_end_other() -> None:
    assert end_other("Hiabc", "abc") is True
    assert end_other("AbC", "HiaBc") is True
    assert end_other("abc", "abXabc") is True
