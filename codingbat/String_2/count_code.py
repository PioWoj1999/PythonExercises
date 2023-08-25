# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.


def main():
    return None


def check_code(str: str) -> bool:
    return str.lower() == "coe"


def count_code(str: str) -> int:
    """
    Function that calculates how many term 'co*e' exists in string.
    """
    countCode = 0
    for i in range(0, len(str) - 3):
        if check_code(str[i] + str[i + 1] + str[i + 3]) is True:
            countCode += 1
    return countCode


if __name__ == "__main__":
    print(count_code("codecodecose"))
