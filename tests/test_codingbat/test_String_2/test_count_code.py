from codingbat.String_2.count_code import count_code


def test_count_code() -> None:
    assert count_code("aaacodebbb") == 1
    assert count_code("codexxcode") == 2
    assert count_code("cozexxcope") == 2
