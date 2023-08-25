# Return the number of times that the string "hi" appears anywhere in the given string.
def main():
    return None


def count_hi(str) -> int:
    """
    Function to calculate how many "hi"'s are in input string.
    """
    countHi = 0
    for i in range(0, len(str) - 1):
        if str[i] + str[i + 1] == "hi":
            countHi += 1
    return countHi


if __name__ == "__main__":
    print(count_hi("hihi"))
