class MyStack(object):

    def __init__(self):
        self._top = None
        self._length = 0
        
        
    def is_empty(self):
        return self._length == 0
        
    def __len__(self):
        return self._length
        
    def __str__(self):
        string_list = []
        current_node = self._top
        while current_node != None:
            string_list.append(str(current_node.data))
            current_node = current_node.next
        return ','.join(string_list)
        
    def peek(self):
        assert self.is_empty() == False, "cannt peek an empty stack"
        return self._top.data
        
    def pop(self):
        assert self.is_empty() == False, "cannt pop an empty stack"
        temp = self._top.data
        self._top = self._top.next
        self._length -= 1
        return temp
    
    def push(self, data):
        new_node = _StackNode(data, self._top)
        self._top = new_node
        self._length += 1
        
        
class _StackNode(object):
    def __init__(self, data, link):
        self.data = data
        self.next = link
        
        
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