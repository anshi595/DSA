#insertion in linked list at benginning
class Node:
    def __init__(self, data):
        self.data=data
        self.next= None

#LinkedList class contains an object of Node class in it
class LinkedList:
    def __init__(self):
        self.head= None
    
    def traversal(self):
        print()
        if self.head is None:
            print("LInked List is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data)
                temp= temp.next
    
    def insert_at_begin(self, data):
        #create a new node
        nNode= Node(data)
        #update the link b/w nNode and old firstNode
        nNode.next=self.head
        #Move the head to point to new Node 
        self.head=nNode


    def insert_at_end(self, data):
        #create a new Node
        nNode= Node(data)
        #if ll is empty then make new node as head
        if self.head is None:
            self.head=nNode
            return
        else:
            #traverse till last node and change next pointer of last node O(N)
            temp=self.head
            while temp.next is not None:
                
                temp=temp.next
            
            temp.next=nNode
    def insert_in_between(self, position, data):
        print() #to print an new line
        #create a new node and put in data
        nNode= Node(data)
        #update the next pointers
        temp= self.head #start
        for i in range(1, position -1):
            temp=temp.next
        
        #Make next of new Node as next of prev_node
        nNode.next= temp.next
        #make next of prev_node as new_node
        temp.next= nNode

    def delete_begin(self):
        if self.head is None:
            return "LL is empty!"
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None #to disconnect the link
    
    def delete_at_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    
    def delete_at_position(self, position):
        prev=self.head
        temp=self.head.next
        for i in range(1, position-1):
            temp=temp.next
            prev=prev.next
        #to disconnect the link
        prev.next=temp.next
        #temp.next=None : no need to do it as garbage collector will collect it and memory will be freed.
        
    

sl=LinkedList()
n1= Node(5)
sl.head=n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next=n3
n4=Node(20)
n3.next=n4
#sl.traversal()
#sl.insert_at_begin(2)
#sl.insert_at_end(25)
sl.traversal()
#sl.insert_in_between(3, 7)
sl.traversal()
sl.delete_begin()
sl.traversal()
sl.delete_at_position(3)
sl.traversal()





