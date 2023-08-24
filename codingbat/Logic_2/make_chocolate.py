# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.


def main():
    return None


def make_chocolate(small, big, goal) -> int:
    howManyBig = big
    restToAdd = goal
    while howManyBig > 0 and restToAdd - 5 > 0:
        howManyBig -= 1
        restToAdd -= 5
    if small >= restToAdd:
        return restToAdd
    else:
        return -1


# TODO: practice
def make_chocolate_2(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - 5 * big
    else:
        remainder = goal % 5

    if remainder <= small:
        return remainder
    return -1


if __name__ == "__main__":
    print(make_chocolate(4, 1, 10))
