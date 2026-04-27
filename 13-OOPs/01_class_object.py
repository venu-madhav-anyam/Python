class Note:
    def __init__(self,title,content):
        self.title = title
        self.content = content
    def print_details(self):
        print(f"{self.title} : {self.content}")

n1 = Note("Meeting Notes","Discuss project status with team")
n2 = Note("Grocery List","Eggs, Milk, Bread")

n1.print_details()
n2.print_details()