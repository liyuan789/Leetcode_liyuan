# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printMiddle(self):
        slow = self.head
        fast = self.head

        if self.head is not None:
            while fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
                slow = slow.next
            print("The middle element is: ", slow.data)


list1 = LinkedList()
list1.push(10)
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)

list1.printMiddle()

