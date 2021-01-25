# Given a sorted (in ascending order) integer array nums of n elements and a target value,
# write a function to search target in nums.
# If target exists, then return its index, otherwise return -1.

def search(nums, target) -> int:
    if nums is None or len(nums) == 0:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print(search([-1, 0, 3, 5, 9, 12], 5))
print(search([-1, 0, 3, 5, 9, 12], 9))

print(search([-1, 0, 3, 5, 9, 12], 4))
print(search([], 5))
print(search(None, 5))
