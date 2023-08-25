# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.


def main():
    return None


def end_other(a: str, b: str) -> bool:
    """
    Check if the char from par: b is at end of par: a. and other way.
    """
    if len(a) > len(b):
        return a.lower().endswith(b.lower())
    else:
        return b.lower().endswith(a.lower())


if __name__ == "__main__":
    print(end_other("HiaBc", "abc"))
