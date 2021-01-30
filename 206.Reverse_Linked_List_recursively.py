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


def reverseLinkedList2(head):
    # Base Case
    # make sure the later head.next.next != null
    if head is None or head.next is None:
        return head   # return new_head N3; 并返回上一层 recursion 停留的位置

    # Recursive Rule
    # sub-problem 里边的箭头已经反转好; 返回 sub-problem 的 new_head
    new_head = reverseLinkedList2(head.next)
    head.next.next = head  # 反转箭头方向；sub-problem head 指向 current node； head is N2
    head.next = None  # 去掉原有箭头；current node's next is set to Null
    return new_head


head_element = Node(1)
head_element.next = Node(2)
head_element.next.next = Node(3)
printLinkedList(head_element)

printLinkedList(reverseLinkedList2(head_element))
