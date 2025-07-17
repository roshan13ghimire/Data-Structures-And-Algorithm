#Binary_Tree

#creating a binary tree

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
class BinaryTree:
    def __init__(self):
        self.root = None
    
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)


#displaying the tree using depth first search

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data,end = " ")
        inorder(node.right)
    
inorder(tree.root)
print("\n")

def preorder(node):
    if node:
        print(node.data,end = " ")
        preorder(node.left)
        preorder(node.right)
preorder(tree.root)
print("\n")

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data,end = " ")
postorder(tree.root)
