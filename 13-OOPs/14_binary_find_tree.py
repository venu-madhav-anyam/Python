class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self,node,value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left,value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right,value)

    def search(self,value):
        return self._search_recursive(self.root,value)
    def _search_recursive(self,node,value):
        if node is None or node.value == value:
            return node is not None
        if value < node.value:
            return self._search_recursive(node.left,value)
        else:
            return self._search_recursive(node.right,value)
        
bst = BST()
for val in [5,3,7,2,4,6,8]:
    bst.insert(val)

print(bst.search(5))

   