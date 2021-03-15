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


def remove_elements1(head, val):
    dummy = Node(0)
    dummy.next = head
    prev = dummy  # prev: record the current node(head)'s prev node
    while head is not None:
        if head.data == val:
            prev.next = head.next
        else:
            prev = head  # otherwise, shift the position
        head = head.next
    return dummy.next


head_ele = Node(1)
head_ele.next = Node(2)
head_ele.next.next = Node(4)
head_ele.next.next.next = Node(6)
head_ele.next.next.next.next = Node(8)
head_ele.next.next.next.next.next = Node(10)

printLinkedList(remove_elements1(head_ele, 6))