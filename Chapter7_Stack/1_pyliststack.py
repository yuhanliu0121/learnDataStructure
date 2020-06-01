class MyStack(object):
    def __init__(self):
        self._stack_list = list()
        
    def is_empty(self):
        return len(self._stack_list) == 0
        
    def __str__(self):
        return str(self._stack_list)
        
    def __len__(self):
        return len(self._stack_list)
        
    def peek(self):
        assert self.is_empty() != True, "stack is empty"
        return self._stack_list[-1]
        
    def pop(self):
        assert self.is_empty() != True, "stack is empty"
        return self._stack_list.pop()
        
    def push(self, item):
        self._stack_list.append(item)
        
        
def main():
    stack = MyStack()
    print("stack is empty?  " + str(stack.is_empty()))
    print("stack length?  " + str(len(stack)))
    print()
    
    print("push 2,2,3,4,5 into stack")
    
    stack.push(2)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    
    print("stack is empty?  " + str(stack.is_empty()))
    print("stack length?  " + str(len(stack)))  
    print()
    
    print('stack.pop(): ' + str(stack.pop()))
    print(stack)
    print()
    
    print("stack.peek(): " + str(stack.peek()))
    print(stack)
    
if __name__ == "__main__":
    main()
    
    