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


def insertNode(head, value):
    new_node = Node(value)  # create a new node

    # Case1: determine if the inserted node is before head
    if head is None or head.data >= value:
        new_node.next = head
        return new_node

    # Case2: insert the new node to the right position
    prev = head  # 一定要有这步：head保持不变, prev用来找插入位置

    # get the insert position: between prev and prev.next
    # 保证 prev.data 一定小于 value; 而 prev.next.data 一定大于等于 value
    while prev.next is not None and prev.next.data < value:
        prev = prev.next

    # insert value between prev and prev.next
    new_node.next = prev.next  # 先记下原来的 prev.next
    prev.next = new_node  # prev 指向新的 new_node
    return head


head_element = Node(1)
head_element.next = Node(2)
head_element.next.next = Node(5)
printLinkedList(insertNode(head_element, 3))

head_element = Node(1)
head_element.next = Node(2)
head_element.next.next = Node(5)
printLinkedList(insertNode(head_element, 0))

head_element = Node(1)
head_element.next = Node(2)
head_element.next.next = Node(5)
printLinkedList(insertNode(head_element, 10))

head_element = None
printLinkedList(insertNode(head_element, 3))