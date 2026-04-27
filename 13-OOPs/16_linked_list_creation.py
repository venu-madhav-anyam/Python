class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self,data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while current.next and current.data != data:
            prev = current
            current = current.next
        if current:
            prev.next = current.next
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


l1 = LinkedList()
l1.insert(10)
l1.insert(20)
l1.display()