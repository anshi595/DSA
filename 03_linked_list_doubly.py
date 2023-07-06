class Node:
    def __init__(self, data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert_at_end(self, data):
        #O(1)
        #this operation inserts items in the end so we have to manipulate the tail node in O(1) time.
        #create a new node
        newNode= Node(data)
        #check is dll is empty if yes --> head and tail will point to same new node
        if self.head is None:
            self.head= newNode
            self.tail=newNode
        
        #there is element in dll. so insert the item in the end of linked list. i.e: manipulate the tail node
        else:
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail=newNode


    def insert_at_head(self, data):
        #O(1)
        #create a node first
        newNode=Node(data)
        #check if dll is empty:
        if self.head is None:
            self.head= newNode
            self.tail=newNode
        #dll has at least one item
        else:
            #newNode previus should be None
            newNode.prev=None
            #Make next of new node as head
            newNode.next=self.head
            #change prev of head node to new node
            self.head.prev=newNode
            #move the head to point to the new node
            self.head=newNode
        
    def insert_at_position(self, data, position):
        #O(N) running time
        #create a node first
        newNode= Node(data)
        temp=self.head
        for i in range(1, position-1):
            if temp is not None:
                temp=temp.next
        
        #if temp is not null then adjust the links
        if temp is not None:
            newNode.next=temp.next
            newNode.prev=temp
            temp.next=newNode
            if temp.next is not None:
                temp.next.prev=newNode

 
    
    def traverse_forward(self):
        temp=self.head
        while temp is not None:
            print("%d" %temp.data)
            temp=temp.next
        print()


    def traverse_backward(self):
        temp=self.tail
        while temp is not None:
            print("%d" %temp.data)
            temp=temp.prev


list=DoublyLinkedList()
list.insert_at_head(5)
list.insert_at_end(10)
list.insert_at_end(15)
#list.insert_at_position(20, 3) #bug here
list.insert_at_end(25)
list.traverse_forward()
list.traverse_backward() #




            




            
            




    

