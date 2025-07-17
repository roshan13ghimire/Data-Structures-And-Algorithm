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
