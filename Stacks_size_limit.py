class Stack:
    def __init__(self,MaxValue):
        self.Maxvalue= MaxValue
        self.list=[]
    

    def __str__(self):
        values=self.list.reverse()
        values=(str(x) for x in self.list)
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list==[]:
            return True
        return False
    
    def isFull(self):
        if len(self.list)==self.Maxvalue:
            return True
        return False
    
    def push(self,value):
        if self.isFull():
            return "Can't Fit more"
        else:
            self.list.append(value)
        
    def pop(self):
        if self.isEmpty():
            return "Nothing to remove"
        else:
            self.list.pop()
    def peek(self):
        if self.isEmpty():
            return "No Element Found"
        else:
            return self.list[-1]
    def delete_stack(self):
        del self.list[:] 

new_stack= Stack(5)
new_stack.push(1)
new_stack.push(2)
new_stack.push(0)
new_stack.pop()
print(new_stack.peek())
print(new_stack.isFull())
print(new_stack)
print(new_stack.isEmpty())
print("/")
new_stack.delete_stack()
print(new_stack.isEmpty())


    

    
