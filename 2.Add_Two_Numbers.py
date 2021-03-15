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


def add_two_numbers(a, b):
    dummy = Node(0)
    cur = dummy
    val = 0

    while a is not None and b is not None and val is not None:
        if a is not None:
            val += a.data
            a = a.next
        if b is not None:
            val += b.data
            b = b.next

        # if the val < 10, cur will remain the same value as it is, and val will take 0
        # if the val >= 10, cur should take val%10, and val will take 1 advance as the next digit will gain from last digit
        cur.next = Node(val % 10)
        val = val // 10
        cur = cur.next

    return dummy.next


head_node1 = Node(1)
head_node1.next = Node(2)
head_node1.next.next = Node(4)

head_node2 = Node(6)
head_node2.next = Node(8)
head_node2.next.next = Node(1)

printLinkedList(add_two_numbers(head_node1, head_node2))