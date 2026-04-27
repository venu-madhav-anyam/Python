class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")

    def is_empty(self):
        return len(self.items) == 0
    
q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
print(q1.dequeue())