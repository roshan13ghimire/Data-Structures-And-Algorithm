#inserting_bst_using_iterative

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.node = None
    
    def insert(self,data):
        if self.node is None:
            self.node =  Node(data)
            return
        
        parent = None
        current = self.node
        while current:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right
                
        
        if data < parent.data:
            parent.left = Node(data)
        else:
            parent.right = Node(data)
        
        
        
        
        
        
tree = BST()
tree.insert(8)
tree.insert(3)
tree.insert(10)
tree.insert(6)

print("Inorder traversal is :")

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end = " ")
        inorder(node.right)
inorder(tree.node)