# Reverse a singly linked list.

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULLv

# create a linked list
# create a class to store linked list by recording the head of the list
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


# create another class to represent each node of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


def printLinkedList(a):
    node = a
    result = f'{node.data}'
    # node = node.next

    while node:
        result += f' -> {str(node.data)}'
        node = node.next
    print(result)


def reverseLinkedList(head_element):
    prev = None
    while head_element is not None:
        # step1: record next
        next_element = head_element.next
        # step2: reverse the link
        head_element.next = prev
        # step3: shift positions
        prev = head_element
        head_element = next_element
    return prev


test = LinkedList([1, 2, 3])
printLinkedList(test.head)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
printLinkedList(head)

printLinkedList(reverseLinkedList(head))

