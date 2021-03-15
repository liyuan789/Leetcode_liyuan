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


def find_middle(head):
    if head is None or head.next is None:
        return head
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def reverse_linked_list(head):
    if head is None or head.next is None:
        return head
    prev = None
    while head is not None:
        # step1: record the next
        next = head.next
        # step2: reverse the link
        head.next = prev
        # step3: shift the positions
        prev = head
        head = next
    return prev


def palindrome(head):
    if head is None or head.next is None:
        return True

    middle = find_middle(head)   # find the middle
    right = reverse_linked_list(middle.next)  # reverse the later half

    while right is not None:
        if head.data != right.data:
            return False
        head = head.next
        right = right.next

    return True


head_ele = Node(1)
head_ele.next = Node(2)
head_ele.next.next = Node(4)
head_ele.next.next.next = Node(6)
head_ele.next.next.next.next = Node(8)
head_ele.next.next.next.next.next = Node(10)

print(palindrome(head_ele))