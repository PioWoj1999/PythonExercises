# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.


def main():
    return None


def average_of_list(num: list):
    """
    Calculate the average of list
    """
    return sum(num) / len(num)


def centered_average(nums: list) -> int:
    """
    Get centered average of list elements.
    """
    nums.remove(max(nums))
    nums.remove(min(nums))
    return int(average_of_list(nums))


if __name__ == "__main__":
    print(centered_average([1, 2, 3, 4, 100]))
