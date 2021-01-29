import random


def QuickSort(array):
    if array is None or len(array) <= 1:
        return array
    quickSort(array, 0, len(array) - 1)
    return array


def quickSort(array, left, right):
    # Base Case
    if left >= right:
        return

    # Recursion Rule
    # firstly, use pivot to partition the array；左半边都比他小，右半边都比他大
    # return pivot index; 保证 pivot 已经在正确位置
    pivot_pos = partition(array, left, right)
    # then, recursively call quickSort function to sort two parts
    # pivot should not be included in any parts
    quickSort(array, left, pivot_pos - 1)
    quickSort(array, pivot_pos + 1, right)


# Use pivot to partition the array; 保证本次 pivot 在正确位置上
def partition(array, left, right):
    pivot_index = pivotIndex(left, right)
    pivot = array[pivot_index]

    # swap the pivot element to the rightmost position
    swap(array, pivot_index, right)
    left_bound = left
    right_bound = right - 1

    while left_bound <= right_bound:
        if array[left_bound] < pivot:  # no swap; move forward
            left_bound += 1
        elif array[right_bound] >= pivot:  # no swap; continue
            right_bound -= 1
        else:
            swap(array, left_bound, right_bound)

    # swap back the pivot element
    swap(array, left_bound, right)
    return left_bound


# Randomly select the pivot in the range of [left, right]
def pivotIndex(left, right):
    return random.randint(left, right)


def swap(array, left, right):
    temp = array[left]
    array[left] = array[right]
    array[right] = temp


print(QuickSort([5, 2, 3, 1]))
print(QuickSort([1, 2, 3, 1]))
print(QuickSort([4, 3, 2, 1]))
print(QuickSort([5, 100, 3, 1]))
print(QuickSort([5, 2, 3, -100]))
