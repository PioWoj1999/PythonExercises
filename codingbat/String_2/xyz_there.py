# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.


def main():
    return None


def xyz_there(str: str) -> bool:
    """
    Return if the string contains 'xyz' string.
    """
    return str.count(".xyz") != str.count("xyz")


if __name__ == "__main__":
    print(xyz_there("abc.xyzxyz"))
