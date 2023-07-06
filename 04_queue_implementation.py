#array implementation of queue:
class Queue:
    def __init__(self):
        self.queue=[]

    def is_empty(self):
        return self.queue==[]
    def queue_size(self):
        return len(self.queue)
    
    def enqueue(self, data):
        #add theb elemenmt in last 
        self.queue.append(data)
    
    def dequeue(self):
        #O{N}
        if self.queue_size() !=0:
            temp=self.queue[0]
            #remove first item from array
            del self.queue[0]
            return temp
    def peek(self):
        return self.queue[0]
    

"""q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.dequeue())"""

class Node():
    def __init__(self, data):
        self.data=data
        self.next=None

class QueueUsingLL():
    def __init__(self):
        self.front=None  #start pointer
        self.rear=None #for last pointer
    def enqueue(self, data):
        newNode=Node(data)
        if self.rear==None:
            self.front=newNode
            self.rear=self.front
        else:
            #to change the pointing from None to newNode
            self.rear.next=newNode
            #to update the rear to newNode
            self.rear=newNode
    
    def dequeue(self):
        if self.front==None:
            return "Queue is Empty!"
        else:
            temp=self.front
            self.front=temp.next
            temp.next=None  #to disconnect the link
            
    def is_Empty(self):
        return self.front==None
    
    def is_size(self):
        temp=self.front
        counte=0
        while temp !=None:
            counter+=1
            temp=temp.next
        return counter
    
    def traverse(self):
        print()
        temp=self.front
        while temp !=None:
            print(temp.data, end=" ")
            temp=temp.next
        
ql=QueueUsingLL()
ql.enqueue(2)
ql.enqueue(6)
ql.traverse()
ql.enqueue(10)
ql.traverse()
ql.dequeue()
ql.traverse()
ql.dequeue()
ql.traverse()


    
            
        




        


        
        
