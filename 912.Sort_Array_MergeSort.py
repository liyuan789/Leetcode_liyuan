
def MergeSort(array):
    if array is None or len(array) <= 1:
        return array
    return mergeSort(array, 0, len(array) - 1)


# Split array into two sub-arrays and mergeSort both sides separately
def mergeSort(array, start, end):
    # Base Case
    if start == end:
        return [array[start]]

    # Recursion Rule
    mid = start + (end - start) // 2
    left_sorted = mergeSort(array, start, mid)
    right_sorted = mergeSort(array, mid + 1, end)

    return merge(left_sorted, right_sorted)


def merge(left_sorted, right_sorted):
    result = []
    left_idx = 0
    right_idx = 0

    # 两边都有剩余; 谁小移谁
    while left_idx < len(left_sorted) and right_idx < len(right_sorted):
        if left_sorted[left_idx] <= right_sorted[right_idx]:
            result.append(left_sorted[left_idx])
            left_idx += 1
        else:
            result.append(right_sorted[right_idx])
            right_idx += 1

    # 左半边有剩余
    while left_idx < len(left_sorted):
        result.append(left_sorted[left_idx])
        left_idx += 1

    # 右半边有剩余
    while right_idx < len(right_sorted):
        result.append(right_sorted[right_idx])
        right_idx += 1

    return result


print(MergeSort([5, 2, 3, 1]))
print(MergeSort([1, 2, 3, 4]))
print(MergeSort([4, 3, 2, 1]))
