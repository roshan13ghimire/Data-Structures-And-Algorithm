class Node():
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
class Doubly():
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
            
    def insertAtLoc(self,data,n):
        new_node = Node(data)
        if n == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
        temp = self.head
        for i in range(n-1):
            temp = temp.next
            if temp is None:
                print("Index out of range")
                return
            
            
        temp1 = temp.next
        temp.next = new_node
        new_node.prev = temp
        new_node.next = temp1
        if temp1:
            temp1.prev = new_node
    
    def deleteAtBegin(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        
        self.head = temp.next
        if self.head:
            self.head.prev = None
        del temp
        
    def deleteAtEnd(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        
        if temp.next is None:
            self.head = None
            del temp
            return
        
        while temp.next is not None:
            temp = temp.next
        temp.prev.next = None
        del temp
    
    def deleteAtLoc(self,n):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        
        if n == 0:
            self.head = temp.next
            if self.head:
                temp.next.prev = None
            del temp
            return
        
        for i in range(n):
            temp = temp.next
            if temp is None:
                print("Index out of range")
                return
        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev
    
    def reverse(self):
        prev_node = None
        temp = self.head
        while temp is not None:
            temp.next, temp.prev = temp.prev,temp.next
            prev_node = temp
            temp = temp.prev
        self.head = prev_node
            
        
    
    def print_list(self):
        if self.head is None:
            print("No element")
            return
        temp = self.head
        while temp is not None:
            print(temp.data , end = "-> ")
            temp = temp.next
        print("None")
        
        
d = Doubly()        
d.insertAtBegin(5)
d.insertAtBegin(10)
d.insertAtEnd(9)
d.insertAtEnd(8)
d.insertAtLoc(7,3)
# d.deleteAtBegin()
# d.deleteAtEnd()
# d.deleteAtLoc(2)
d.print_list()
d.reverse()
d.print_list()
