# Write an efficient algorithm that searches for a value in an m x n matrix.

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

def searchMatrix(matrix, target):
    m = len(matrix)
    if m == 0:
        return False  # no rows means matrix is empty
    n = len(matrix[0])

    # binary search
    left = 0
    right = m * n - 1

    while left <= right:  # condition
        mid_idx = left + (right - left) // 2
        mid_row = mid_idx // n
        mid_col = mid_idx % n
        mid_element = matrix[mid_row][mid_col]
        if target == mid_element:
            return True
        elif target < mid_element:
            right = mid_idx - 1
        else:
            left = mid_idx + 1

    return False  # target not found


print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 20))
print(searchMatrix([[1, 3, 5, 7], [23, 30, 34, 60]], 20))
print(searchMatrix([], 20))

