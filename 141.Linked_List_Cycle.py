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

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def detectLoop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return "Found Loop"
        return "No Loop"


# Driver program for testing
list2 = LinkedList()
list2.push(20)
list2.push(4)
list2.push(15)
list2.push(10)

# Create a loop for testing
list2.head.next.next.next.next = list2.head
print(list2.detectLoop())
