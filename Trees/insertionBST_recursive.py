#binary_search_tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,root,data):
        if root is None:
            root = Node(data)
            return root
        
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        else:
            pass
    
        return root

        
        
tree = BST()
r = tree.root
r = tree.insert(r,8)
r = tree.insert(r,3)
r = tree.insert(r,10)
r = tree.insert(r,6)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.data,end = " ")
        inorder(node.right)
    
inorder(r)
