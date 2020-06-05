class CircularLinkedList(object):
    def __init__(self):
        self._list_reference = None
        
    def show(self):
        string_list = list()
        
        current_node = self._list_reference
        done = current_node is None
        
        while not done:
            current_node = current_node.next
            string_list.append(current_node.data)
            done = current_node is self._list_reference
            
        return str(string_list)
        
    def __contains__(self, target):
        if self._list_reference is not None:
            if target <= self._list_reference.data and target >= self._list_reference.next.data:

               current_node = self._list_reference
               done = False
                
               while not done:
                    current_node = current_node.next
                    if current_node.data == target:
                        return True
                    else:
                        done = current_node is self._list_reference
            
        return False
        
    def add(self, data):
        new_node = _ListNode(data)
        
        if self._list_reference is None:     
            new_node.next = new_node
            self._list_reference = new_node
        
        elif data < self._list_reference.next.data:
            new_node.next = self._list_reference.next
            self._list_reference.next = new_node
            
        elif data > self._list_reference.data:      
            new_node.next = self._list_reference.next
            self._list_reference.next = new_node
            self._list_reference = new_node
            
        else:
            pre_node = None
            current_node = self._list_reference.next
            done  = self._list_reference is None
            
            while not done:
                pre_node = current_node
                current_node = current_node.next
                
                done = current_node.data > data or current_node is self._list_reference
                
            pre_node.next = new_node
            new_node.next = current_node
            
    def remove(self, data):
        if self._list_reference is not None:
            if data >= self._list_reference.next.data and data <= self._list_reference.data:
                
                pre_node = None
                current_node = self._list_reference
                done = False
                
                while not done:
                    pre_node = current_node
                    current_node = current_node.next
                    done = current_node.data >= data or current_node is self._list_reference
                
                if current_node.data == data:
                    if current_node == self._list_reference.next:
                        self._list_reference.next = current_node.next
                        
                    elif current_node == self._list_reference:
                        pre_node.next = self._list_reference.next
                        self._list_reference = pre_node
                    
                    else:
                        pre_node.next = current_node.next
            
        
class _ListNode(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
        
def main():
    print("create a CircularLinkedList")
    dlist = CircularLinkedList()   
    print("dlist: %s" % dlist.show())
    print()
    print("100 in list? " + str(100 in dlist))
    print()
    print("remove 0")
    dlist.remove(0)
    print(dlist.show())
    print()
    
    
    print("add 0 0 1 9 6 3 to the list")
    dlist.add(0)
    dlist.add(0)
    dlist.add(1)
    dlist.add(9)
    dlist.add(6)
    dlist.add(3)
    print(dlist.show())
    print()
    
    print("100 in list? " + str(100 in dlist))
    print()
    print("0 in list? " + str(0 in dlist))
    print()
    print("3 in list? " + str(3 in dlist))
    print()
    print("9 in list? " + str(9 in dlist))
    print()
    
    print("remove 0")
    dlist.remove(0)
    print(dlist.show())
    print()
    
    print("remove 3")
    dlist.remove(3)
    print(dlist.show())
    print()
    
    print("remove 9")
    dlist.remove(9)
    print(dlist.show())
    print()
    
    print("remove 100")
    dlist.remove(100)
    print(dlist.show())
    
if __name__ == "__main__":
    main()