# Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
    counter = 0
    for i in nums:
        if i == 9:
            counter += 1
    return counter
