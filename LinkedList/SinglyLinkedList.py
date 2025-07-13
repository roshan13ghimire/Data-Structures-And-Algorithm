class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        
    def insertAtBegin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node
            new_node.next = None
    
    def insertAtLoc(self,data,n):
        new_node = Node(data)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        temp = self.head
        for i in range(n-1):
            if temp == None:
                print("Index is higher than the list")
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        
    def length(self):
        if self.head == None:
            return 0
        c = 0
        temp = self.head
        while(temp != None):
            temp = temp.next
            c += 1
        return c
        
    def reverse(self):
        prev = None
        temp = self.head
        while temp is not None:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.head = prev

    def deleteAtBegin(self):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.next is None:
            del self.head
            self.head = None
            return
        
        temp = self.head
        self.head = temp.next
        del temp
    
    def deleteAtEnd(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        if self.head.next is None:
            del self.head
            self.head = None
            return
        
        temp = self.head
        while temp.next is not None:
            temp1 = temp
            temp = temp.next
        temp1.next = None
        del temp
        
    def deleteAtLoc(self,n):
        if self.head is None:
            print("Linked List is empty")
            return
        
        if n == 0:
            temp = self.head
            self.head = temp.next
            del temp
            return
        
        temp = self.head
        temp1 = None
        for i in range(n): 
            temp1 = temp
            temp = temp.next
            if temp is None:
                print("Index out of range")
                return
        temp1.next = temp.next
        del temp
        
        
    def print_list(self):
        if self.head == None:
            print("No element Found")
        else:
            temp = self.head
            while(temp != None):
                print(temp.data,end = "-> ")
                temp = temp.next
            print("None")
        
l = LinkedList()
l.insertAtBegin(5)
l.insertAtBegin(6)
l.insertAtBegin(7)
l.insertAtEnd(8)
l.insertAtEnd(9)
l.insertAtLoc(10,3)

l.print_list()

# print(l.length())

# l.reverse()

# l.deleteAtBegin()
# l.deleteAtEnd()
l.deleteAtLoc(4)
l.print_list()
