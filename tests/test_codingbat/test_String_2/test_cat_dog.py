from codingbat.String_2.cat_dog import check_if_cat, check_if_dog, cat_dog


def test_if_cat() -> None:
    assert check_if_cat("cat") is True
    assert check_if_cat("cad") is False


def test_if_dog() -> None:
    assert check_if_dog("dor") is False
    assert check_if_dog("dog") is True


def test_cat_dog() -> None:
    assert cat_dog("1cat1cadodog") is True
    assert cat_dog("catcat") is False
    assert cat_dog("catdog") is True
