#searching_in_bst_using_recursion

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
    
    def search(self,node,val):
        if node is None:
            return None
        
        if val < node.data:
            return self.search(node.left,val)
            
        elif val > node.data:
            return self.search(node.right,val)
        else:
            return node
            

tree = BST()
n = tree.node
n = tree.insert(n,8)
n = tree.insert(n,3)
n = tree.insert(n,10)
n = tree.insert(n,6)

result = tree.search(n,6)
if(result):
    print("Element Found")
else:
    print("Element not Found")