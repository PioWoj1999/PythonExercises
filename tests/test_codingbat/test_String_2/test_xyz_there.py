from codingbat.String_2.xyz_there import xyz_there


def test_str_contains_xyz() -> None:
    assert xyz_there("xyz.abc") is True
    assert xyz_there("abcxyz") is True
    assert xyz_there("abc.xyz") is False
    assert xyz_there("abc.xyzxyz") is True
