#deletion_bst_using_recursion

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
            
    def deletion(self,node,data):
        if node is None:
            return None
        
        if data < node.data:
            node.left = self.deletion(node.left,data)
        elif data > node.data:
            node.right = self.deletion(node.right,data)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                mini = self.find_min(node.right)
                node.data = mini.data
                node.right = self.deletion(node.right, mini.data)
        
        return node
        
    def find_min(self,node):
        current = node
        while current.left is not None:
            current = current.left
        return current
            
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data, end = " ")
            self.inorder(node.right) 
        

tree = BST()
n = tree.node
n = tree.insert(n,50)
n = tree.insert(n,30)
n = tree.insert(n,70)
n = tree.insert(n,20)
n = tree.insert(n,40)
n = tree.insert(n,60)
n = tree.insert(n,80)


print("Inorder traversal is :")
tree.inorder(n)
print("\n")
n = tree.deletion(n,50)
print("\nAfter deletion")
tree.inorder(n)