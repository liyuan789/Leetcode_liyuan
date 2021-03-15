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


# one is the head node of first Linked List
# two is the head node of second Linked List
def merge_two_sorted_list(one, two):
    dummy = Node(0)  # return dummy.next; what dummy is doesn't matter
    cur = dummy

    # 当1和2都有剩余时，谁小移谁，接元素
    while one is not None and two is not None:
        if one.data <= two.data:
            cur.next = one
            one = one.next
        else:
            cur.next = two
            two = two.next
        cur = cur.next

    # 当只有一边剩余或者都没有剩余时，直接链接有剩余的部分
    if one is not None:
        cur.next = one  # 若1有剩余：直接接上1的所有剩余
    else:
        cur.next = two  # 若1没有生育：直接街上2的所有剩余

    return dummy.next   # cur 在不断变化，而 dummy 保持不变


head_element1 = Node(1)
head_element1.next = Node(2)
head_element1.next.next = Node(5)

head_element2 = Node(1)
head_element2.next = Node(3)
head_element2.next.next = Node(4)

printLinkedList(merge_two_sorted_list(head_element1, head_element2))