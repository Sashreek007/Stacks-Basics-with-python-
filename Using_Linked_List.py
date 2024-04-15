class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head= None
    
    def __iter__(self):
        temp=self.head
        while temp:
            yield temp
            temp = temp.next
        
    

class Stack:
    def __init__(self):
        self.LinkedList= LinkedList()
    
    def __str__(self):
        values=(str(x.value) for x in self.LinkedList)
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.LinkedList.head==None:
            return True
        return False

    def push(self,value):
        new_node=Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head=new_node
        else:
            new_node.next=self.LinkedList.head
            self.LinkedList.head=new_node
    def pop(self):
        if self.isEmpty():
            return"No Value found"
        else:
            poped=self.LinkedList.head
            self.LinkedList.head=self.LinkedList.head.next
            return poped.value
    def peek(self):
        if self.isEmpty():
            return"No Value found"
        else:
            poped=self.LinkedList.head
            return poped.value
        
    def delete(self):
        self.LinkedList.head=None
        

   
new_stack= Stack()
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
print(new_stack.pop())
print(new_stack.peek())
print("/")
print(new_stack)
new_stack.delete()
print(new_stack)

