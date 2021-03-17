# Find the smallest k elements in an unsorted array
# assumptions:
# 1. array is not None
# 2. k >= 0
# 3. k <= array.length


# Method1: K sized max heap
import heapq


def kSmallestElements(elements, k):
    """
    :type elements: list of int
    :type k: int
    :rtype: list of int
    """
    max_heap = MaxHeap()

    for element in elements:
        max_heap.add(element)
        print(max_heap.to_list())
        if max_heap.size() == k + 1:
            max_heap.poll()
    print(max_heap.to_list())
    return max_heap.to_list()


# Python's heapq is a minimal heap
class MaxHeap:
    def __init__(self):
        self.data = []

    def peek(self):
        return -self.data[0]

    def add(self, val):
        heapq.heappush(self.data, -val)

    def poll(self):
        return -heapq.heappop(self.data)

    def to_list(self):
        return list(map(lambda item: -item, self.data))

    def size(self):
        return len(self.data)


# kSmallestElements([3, 1, -2, 5, 7], 2)
kSmallestElements([-2, 1, 6, 3, 4, 10, 2, 1], 5)