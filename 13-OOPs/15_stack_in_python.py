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
    
s = Stack()
s.push(10)
s.push(20)
print(s.pop())