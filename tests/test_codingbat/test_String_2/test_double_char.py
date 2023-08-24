from codingbat.String_2.double_char import double_char


def test_double_char():
    assert double_char("The") == "TThhee"
    assert double_char("AAbb") == "AAAAbbbb"
    assert double_char("Hi-There") == "HHii--TThheerree"
