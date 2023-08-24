# Given a string, return a string where for every char in the original, there are two chars.
def main():
    return None


def double_char(str):
    doubleChar = ""
    for i in str:
        doubleChar += i * 2
    return doubleChar


if __name__ == "__main__":
    print(double_char("The"))
