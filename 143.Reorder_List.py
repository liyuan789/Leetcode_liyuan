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


# find the middle node
def middle(head_element):
    slow = fast = head_element
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


# reverse the second half from the list
# 1->2->3->4->5->6 to 1->2->3->6->5->4
def reverse(head_element):
    if head_element is None or head_element.next is None:
        return head_element
    prev = None
    while head_element is not None:
        next = head_element.next  # step1: record the next
        head_element.next = prev  # step2: reverse the link
        prev = head_element  # step3: shift positions
        head_element = next
    return prev


# merge two 'sorted' linked lists
# 1->2->3 6->5->4 to 1->6->2->5->3->4
def merge(one, two):
    dummy = Node(0)
    cur = dummy

    while one is not None and two is not None:
        cur.next = one
        one = one.next
        cur.next.next = two
        two = two.next
        cur = cur.next.next

    if one is not None:
        cur.next = one
    else:
        cur.next = two
    return dummy.next


def reorder_list(head_element):
    if head_element is None or head_element.next is None:
        return head_element

    mid = middle(head_element)
    one = head_element
    two = mid.next
    mid.next = None
    temp = reverse(two)

    return merge(one, temp)


head = Node(1)
head.next = Node(2)
head.next.next = Node(4)
head.next.next.next = Node(6)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(10)

printLinkedList(reorder_list(head))
