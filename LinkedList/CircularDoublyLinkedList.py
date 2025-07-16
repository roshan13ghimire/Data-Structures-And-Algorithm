#Circular Doubly Linked list

class Node():
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
class CircularDoubly():
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self,data):
        new_node = Node(data)
        if self.head is None:
            new_node.prev = new_node
            new_node.next = new_node
            self.head = new_node
            return
        temp = self.head.prev
        
        temp.next = new_node
        new_node.prev = temp
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            new_node.prev = new_node
            new_node.next = new_node
            self.head = new_node
            return
        temp = self.head
        
        temp = temp.prev
        new_node.next = self.head
        new_node.prev = temp
        temp.next = new_node
        self.head.prev = new_node
    
    def insertAtLoc(self,data,n):
        new_node = Node(data)
        temp = self.head
        if n == 0:
            if self.head is None:
                new_node.prev = new_node
                new_node.next = new_node
                self.head = new_node
                return
            new_node.next = temp
            new_node.prev = temp.prev
            temp.prev.next = new_node
            temp.prev = new_node
            self.head = new_node
            return
            
        for i in range(n-1):
            temp = temp.next
            if temp == self.head:
                print("Index Out of Range")
                return
        new_node.next = temp.next
        new_node.prev = temp
        temp.next = new_node
        new_node.next.prev = new_node
        
    def deleteAtBegin(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head 
        if temp.next == self.head:
            self.head = None
            del temp
            return
        
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        self.head = temp.next
        
        del temp
    

    
    def deleteAtEnd(self):
        if self.head is None:
            print("List is empty")
            return
        
        temp = self.head 
        if temp.next == self.head:
            self.head = None
            del temp
            return
        
        last = temp.prev
        last.prev.next = self.head
        self.head.prev = last.prev
        
        del last
    
    
    def deleteAtLoc(self,n):
        if self.head is None:
            print("List is empty")
            return
        
        temp = self.head
        if n == 0:
            temp = self.head
            if self.head.next == self.head:
                self.head = None
                del temp
                return
            
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            self.head = temp.next
            
            del temp
            return
                
        
        for i in range(n):
            temp = temp.next
            if temp == self.head:
                print("Index Out Of Range")
                return
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        
        del temp
    
    def reverse(self):
        if self.head is None or self.head.next == self.head:
            return
        prev_node = None
        temp = self.head
        while temp.next is not self.head:
            temp.prev, temp.next = temp.next, temp.prev
            prev_node = temp
            temp = temp.prev
        temp.prev, temp.next = temp.next, temp.prev
        prev_node = temp
        self.head = prev_node
    
    
    def print_list(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp.next is not self.head:
            print(temp.data, end = "-> ")
            temp = temp.next
        print(temp.data, end = "-> ")
        print("Head")

c = CircularDoubly()
c.insertAtBegin(2)
c.insertAtBegin(3)
c.insertAtBegin(4)
c.insertAtEnd(1)
c.insertAtLoc(5,4)
c.print_list()
# c.deleteAtEnd()
# c.deleteAtLoc(0)

c.reverse()
c.print_list()
        
        
