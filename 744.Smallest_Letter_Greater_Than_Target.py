def nextGreatestLetter(letters, target):
    left = 0
    right = len(letters) - 1

    if letters[-1] <= target:
        return letters[0]

    while left <= right:
        mid = left + (right - left) // 2
        if letters[mid] == target:
            return letters[mid + 1]
        elif letters[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return letters[left]


print(nextGreatestLetter(['c', 'f', 'j'], 'g'))
print(nextGreatestLetter(['c', 'f', 'j'], 'c'))
print(nextGreatestLetter(['c', 'f', 'j'], 'f'))
print(nextGreatestLetter(['c', 'f', 'j'], 'j'))
print(nextGreatestLetter(['c', 'f', 'j'], 'g'))


def nextGreatestLetter2(letters, target):
    # corner case:['c', 'f', 'j']; target = 'k'
    if letters[-1] <= target:
        return letters[0]

    left = 0
    right = len(letters) - 1

    # left < right
    while left < right:
        mid = left + (right - left) // 2
        if letters[mid] > target:
            right = mid
        else:
            left = mid + 1

    # left == right: ['c', 'f', 'j']; target='g'
    if letters[left] > target:
        return letters[left]
