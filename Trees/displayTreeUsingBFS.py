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




#displaying the tree using breadth first search

from collections import deque

def bfs(node):
    if not node:
        print("Tree is Empty")
        return
    
    queue = deque()
    queue.append(node)
    
    while queue:
        current = queue.popleft()
        print(current.data,end = " ")

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    

bfs(tree.root)
    
    
    
    
        
