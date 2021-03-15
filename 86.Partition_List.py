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


def partition_list(head, target):
    if head is None or head.next is None:
        return head

    # Step1: create two dummy heads
    dummy1 = Node(0)
    dummy2 = Node(0)
    cur_small = dummy1
    cur_large = dummy2

    # Step2: iterate comparing over every single element to the target's value
    while head is not None:
        if head.data < target:
            cur_small.next = head
            cur_small = cur_small.next
        else:
            cur_large.next = head
            cur_large = cur_large.next
        head = head.next

    # Step3: concatenate the tail of small to the head of large
    cur_small.next = dummy2.next

    # Step4: the tail of large should be list.next = None
    cur_large.next = None
    return dummy1.next


head_node = Node(1)
head_node.next = Node(8)
head_node.next.next = Node(2)
head_node.next.next.next = Node(5)
head_node.next.next.next.next = Node(7)
head_node.next.next.next.next.next = Node(3)

printLinkedList(partition_list(head_node, 6))
