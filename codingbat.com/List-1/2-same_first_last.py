# Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
def same_first_last(nums):
    if len(nums) == 1 or nums[0] == nums[-1]:
        return True
    else:
        return False


# TODO: practice
# print(same_first_last([1, 2, 3]))
# def same_first_last(nums):
#   return len(nums) >= 1 and nums[0] == nums[-1]
