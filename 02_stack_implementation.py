#using an array
class Stack():
    def __init__(self):
        self.stack= []
    
    def push(self, data): # insert item O(1)
        self.stack.append(data)
    def pop(self): #remove item 
        if self.stack_size !=0:
            data= self.stack[-1] #fetch last element
            del self.stack[-1]
            return data
        else:
            #stack is empty
            return -1
    def peek(self): #O(1)
        return self.stack[-1]
    
    def is_Empty(self): #O(1)
        if self.stack==[]:
            return True
        else:
            return False
    
    def stack_size(self):
        return len(self.stack)
    

"""s=Stack()
s.push(1)
s.push(2)
s.push(3)
print("The popped element is: ", s.pop())
print(s.is_Empty())
print(s.stack_size())"""

# using linked list
class Node():
    def __init__(self, data):
        self.next=None
        self.data=data

class StackUsingLL():
    def __init__(self):
        self.head=None
    
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        #check if stack is empty. if true then first node will be its head
        if self.head is None:
            self.head=Node(data)
            
        
        else:
            #create a new node
            n=Node(data)
            #update the link
            n.next=self.head
            #update head
            self.head=n
    
    def pop(self):
        
        if self.isEmpty():
            return "Stack is Empty"
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
        
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            return "No elements in stack to peek"
        else:
            return self.head.data
    
    def display(self):
        temp=self.head
        if self.isEmpty():
            return "Blank Stack"
        else:
            while temp is not None:
                print(temp.data, end=" ")
                temp=temp.next
        return
    
s=StackUsingLL()
s.push(12)
s.push(34)
s.push(50)
s.push(67)
s.display()
print("\n", s.pop())
print(s.pop())
s.display()











