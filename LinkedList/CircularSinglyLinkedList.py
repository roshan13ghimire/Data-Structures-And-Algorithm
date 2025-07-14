#Circular Singly Linked List

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
class CircularSingly():
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return
        temp = self.head
        while temp.next is not self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
        self.head = new_node
        
        
    def print_list(self):
        if self.head is None:
            print("List is Empty")
            return
        temp = self.head
        while True:
            print(temp.data, end = "-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("Head")
        
        
        
        
c = CircularSingly()
c.insertAtBegin(5)
c.insertAtBegin(10)
c.insertAtBegin(15)
c.insertAtBegin(20)
c.print_list()
