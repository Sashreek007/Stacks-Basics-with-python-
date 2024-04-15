
class StackList:
    def __init__(self):
        self.list=[]

    def __str__(self):
        values=self.list.reverse()
        values=(str(x) for x in self.list)
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list:
            return False
        return True
    
    def push(self,value):
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




new_stack= StackList()
new_stack.push(1)
new_stack.push(2)
new_stack.push(0)
new_stack.pop()
print(new_stack.peek())
print(new_stack.isEmpty())
new_stack.delete_stack()
print(new_stack.isEmpty())
print(new_stack)