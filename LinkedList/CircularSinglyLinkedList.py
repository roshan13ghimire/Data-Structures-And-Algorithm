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
        
    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return
        temp = self.head
        while temp.next is not self.head:
            temp = temp.next
        new_node.next = self.head
        temp.next = new_node
    
    def insertAtLoc(self,data,n):
        new_node = Node(data)
        temp = self.head
        if self.head is None: 
            if n == 0:
                self.head = new_node
                self.head.next = self.head
            else:
                print("Index out of range")
            return
        
        if n == 0:
            while temp.next is not self.head:
                temp = temp.next
                
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node
            return
            
        for i in range(n-1):
            temp = temp.next
            if temp == self.head:
                print("Index out of range")
                return
        new_node.next = temp.next
        temp.next = new_node
        
    def deleteAtBegin(self):
        if self.head is None:
            print("List is empty")
            return
        
        temp = self.head
        if temp.next == self.head:
            self.head = None
            del temp
            return
        
        temp1 = temp
        while temp.next is not self.head:
            temp = temp.next
            
        self.head = temp1.next
        temp.next = temp1.next
        del temp1
    
    def deleteAtEnd(self):
        if self.head is None:
            print("List is empty")
            return
        
        temp = self.head
        if temp.next == self.head:
            self.head = None
            del temp
            return
        
        temp1 = None
        while temp.next is not self.head:
            temp1 = temp
            temp = temp.next
        
        temp1.next = self.head
        del temp
    
    def deleteAtLoc(self,n):
        if self.head is None:
            print("List is empty")
            return
        
        temp = self.head
        
        if n == 0:
            if temp.next == self.head:
                self.head = None
                del temp
                return
            
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = self.head.next
            last.next = self.head
            del temp
            return
        
        for i in range(n):
            temp1 = temp
            temp = temp.next
            if temp == self.head:
                print("Index out of range")
                return
        
        temp1.next = temp.next
        del temp
    
    def print_list(self):
        if self.head is None:
            print("List is Empty")
            return
        temp = self.head
        while temp.next is not self.head:
            print(temp.data, end = "-> ")
            temp = temp.next
            
        print(temp.data, end=" -> ")
        print("Head")
        
        
        
        
c = CircularSingly()
c.insertAtBegin(5)
c.insertAtBegin(10)
c.insertAtBegin(15)
c.insertAtEnd(20)
c.insertAtLoc(25,1)
c.print_list()
# c.deleteAtBegin()
# c.deleteAtEnd()
c.deleteAtLoc(0)
c.print_list()
