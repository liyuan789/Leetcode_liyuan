import heapq


def kLargestHeap(elements, k):
    """
    :type elements: list of int
    :type k: int
    :rtype: int
    """
    # To create a heap, use a list initialized to []
    pq = elements[:k]  # use priority queue to hold k-largest elements
    # right now, pq contains the first k elements

    # heapify(): transform a list into a heap
    heapq.heapify(pq)
    # right now, pq contains the first k (heapified) elements

    # keep push (n-k) new element into the pq and pop the (n-k) minimal one
    for element in elements[k:]:
        heapq.heappush(pq, element)
        heapq.heappop(pq)
    # right now, pq contains the largest k elements

    # return the top(smallest) element of the pq which is the k's largest number
    return pq[0]


print(kLargestHeap([1, 2, 3, 4, 5], 2))
print(kLargestHeap([5, 4, 3, 2, 1], 2))
# print(kLargestHeap([-2, 1, 6, 3, 4, 10, 2, 1], 2))
# print(kLargestHeap([-2, 1, 6, 3, 4, 10, 2, 1], 3))
# print(kLargestHeap([-2, 1, 6, 3, 4, 10, 2, 1], 4))
# print(kLargestHeap([-2, 1, 6, 3, 4, 10, 2, 1], 5))
