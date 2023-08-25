# Return True if the string "cat" and "dog" appear the same number of times in the given string.


def main():
    return None


def check_if_cat(str: str) -> bool:
    """
    Validate if the input string is cat.
    """
    return str == "cat"


def check_if_dog(str: str) -> bool:
    """
    Validate of the input string is dog.
    """
    return str == "dog"


def cat_dog(str: str) -> bool:
    """
    Function to return if dog and cat appears in the string the same amount of times.
    """
    countCat, countDog = 0, 0
    for i in range(0, len(str) - 2):
        checkStr = str[i] + str[i + 1] + str[i + 2]
        if check_if_cat(str=checkStr):
            countCat += 1
        elif check_if_dog(str=checkStr):
            countDog += 1
        else:
            continue
    return countDog == countCat


if __name__ == "__main__":
    print(cat_dog("catdog"))
