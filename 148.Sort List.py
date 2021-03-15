class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return str(nodes)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


def printLinkedList(a) -> LinkedList:
    node = a
    result = f'{node.data}'
    node = node.next

    while node:
        result += f' -> {str(node.data)}'
        node = node.next
    print(result)


def middle_list(head):
    if head is None or head.next is None:
        return head

    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge_list(one, two):
    dummy = Node(0)
    curr = dummy

    while one is not None and two is not None:
        if one.data <= two.data:
            curr.next = one
            one = one.next
        else:
            curr.next = two
            two = two.next
        curr = curr.next

    if one is not None:
        curr.next = one
    else:
        curr.next = two

    return dummy.next


def merge_sort_list(head):
    if head is None or head.next is None:
        return head

    # Step1: split the list into two halves
    mid = middle_list(head)
    right = mid.next
    mid.next = None

    # Step2: recursively sort each half
    left = merge_sort_list(head)
    right = merge_sort_list(right)

    # Step3: combine two halves
    return merge_list(left, right)


head_node = Node(1)
head_node.next = Node(2)
head_node.next.next = Node(4)
head_node.next.next.next = Node(6)
head_node.next.next.next.next = Node(8)
head_node.next.next.next.next.next = Node(10)

printLinkedList(merge_sort_list(head_node))