# Selection Sort
# Given an array of integers, sort the elements in the array in ascending order
def swap(nums, a, b):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp
    return


def selectSort(nums):
    if nums is None or len(nums) <= 1:
        return nums

    min_idx = 0
    while min_idx <= len(nums) - 1:
        for i in range(min_idx, len(nums)):
            if nums[i] < nums[min_idx]:
                swap(nums, min_idx, i)
        min_idx += 1

    return nums


print(selectSort([5, 2, 3, 1]))
print(selectSort([5, 2, 3, 1, -2]))
print(selectSort([1]))
print(selectSort([]))
