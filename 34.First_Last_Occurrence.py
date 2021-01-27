# First, find the index whose element is equal to the target value
def binarySearch(nums, target):
    if nums is None or len(nums) == 0:
        return -1
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1   # otherwise, right is always larger than left
        else:
            left = mid + 1    # otherwise, we would continue while loop forever

    if nums[right] < target or nums[left] > target:
        return -1


# Then find the first and last occurrence of target
def searchRange(nums, target):
    pivot = binarySearch(nums, target)
    if pivot == -1:
        return [-1, -1]

    left = pivot - 1
    right = pivot
    result = []

    while left >= 0 and nums[left] == target:  # avoid index out of range firstly
        left -= 1
    result.append(left + 1)
    while right <= len(nums) - 1 and nums[right] == target:
        right += 1
    result.append(right - 1)

    return result


print(searchRange([5, 7, 8, 8, 8, 10], 8))   # [2,4]
print(searchRange([5, 7, 7, 7, 8, 10], 7))   # [1,3]
print(searchRange([5, 7, 7, 8, 8, 10], 10))  # [5]
print(searchRange([5, 7, 7, 8, 8, 10], 5))   # [0]
print(searchRange([5, 7, 7, 8, 8, 10], 100))
print(searchRange([5, 7, 7, 8, 8, 10], -100))
print(searchRange([], 8))




