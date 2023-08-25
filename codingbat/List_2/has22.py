# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
def main():
    return None


def has22(nums: list) -> bool:
    for i in range(0, len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False


if __name__ == "__main__":
    print(has22([1, 2, 2]))
