#inserting_bst_using_recursion

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.node = None
        
    def insert(self,node,data):
        if node is None:
            return Node(data)
        
        if data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return node

tree = BST()
n = tree.node
n = tree.insert(n,8)
n = tree.insert(n,3)
n = tree.insert(n,10)
n = tree.insert(n,6)

print("Inorder traversal is :")

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end = " ")
        inorder(node.right)
inorder(n)