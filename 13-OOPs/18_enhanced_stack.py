class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Cannot pop from empty stack"
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack: ",self.items)
    
s = Stack()
s.push(10)
s.push(20)
s.display()