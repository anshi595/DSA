#reverse a linked list using iterative method
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def reverse(self):
        current=self.head
        forward=None
        prev=None
        while(current !=None):
            forward=current.next
            current.next=prev
            prev=current
            current=forward
        
        self.head=prev
        
            
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
    


    def traversal(self):
        #print()
        if self.head is None:
            print("LInked List is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data)
                temp= temp.next
    

ll=LinkedList()
ll.insert_at_end(13)
ll.insert_at_end(15)
ll.insert_at_end(27)
ll.traversal()
ll.reverse()
print()
ll.traversal()



    
    
#reverse a linked list using recursion
#print elemenrs of lkinked list in forward and reverse ordr using recursion

