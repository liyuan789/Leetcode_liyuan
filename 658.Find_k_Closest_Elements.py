def binarySearch(arr, x):  # find the closest left and right index
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    # avoid out of range
    if right < 0:
        return 0
    if left > len(arr) - 1:
        return len(arr) - 1

    if abs(arr[left] - x) < abs(arr[right] - x):
        return left
    else:
        return right


def findClosestElements(arr, k, x):   # k closets elements; x is the target value
    if arr is None or len(arr) == 0:
        return arr

    pivot = binarySearch(arr, x)
    left = pivot - 1
    right = pivot + 1
    result = [arr[pivot]]

    # move left or right which is smaller
    while len(result) < k:

        if abs(arr[left] - x) <= abs(arr[right] - x):
            result.append(arr[left])
            left -= 1
        else:
            result.append(arr[right])
            right += 1

    return result


print(findClosestElements([1, 2, 3, 4, 5], 2, 3))
print(findClosestElements([1, 2, 3, 4, 5], 3, 3))
print(findClosestElements([1, 2, 3, 4, 5], 1, 2))
print(findClosestElements([1, 2, 3, 4, 5], 2, 0.1))


