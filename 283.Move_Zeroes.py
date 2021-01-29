# Question 1
# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
def swap(nums, a, b):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp
    return


def move_to_end(nums, start, end):
    for i in range(start, end):
        swap(nums, i, i + 1)


def moveZeroes(nums):
    zeros = 0
    for i in range(len(nums) - 1):
        num = nums[i]
        if num != 0:
            continue
        move_to_end(nums, i, len(nums) - zeros - 1)
        zeros += 1


data = [0, 1, 0, 3, 5]
moveZeroes(data)
print(data)


# Question2
# Given an array of integers, move all the 0s to the right end of the array
# the relative order of the elements in the original array does not need to be maintained
def moveZero(array):
    if array is None or len(array) <= 1:
        return array

    left = 0
    right = len(array) - 1
    while left <= right:
        if array[left] != 0:
            left += 1
        elif array[right] == 0:
            right -= 1
        else:
            swap(array, left, right)
            left += 1
            right -= 1
    return array


def swap(array, a, b):
    tmp = array[a]
    array[a] = array[b]
    array[b] = tmp
