class DoublyLinkedLIst(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._probe = None
        
    def __contains__(self, target):
        if self._head is None or target < self._head.data or target > self._tail.data:
            return False
        elif self._probe is None:
            self._probe = self._head
            
        if target > self._probe.data:
            while self._probe is not None and self._probe.data < target:
                self._probe = self._probe.next
        else:
            while self._probe is not None and self._probe.data > target:
                self._probe = self._probe.prev
            
        if self._probe.data == target:
            return True
        else:
            return False


    def add(self, data):
        new_node = _DoublyLinkedListNode(data)
        if self._head is None:
            self._head = new_node
            self._tail = self._head
            self._probe = self._head
            
        elif data <= self._head.data:
            self._head.prev = new_node
            new_node.next = self._head
            self._head = new_node
        
        elif data >= self._tail.data:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
            
        else:
            current_node = self._head
            while current_node is not None and current_node.data < data:
                current_node = current_node.next  
            
            new_node.next = current_node
            new_node.prev = current_node.prev
            
            current_node.prev.next = new_node
            current_node.prev = new_node
            
        
    def show(self, reverse=False):
        string_list = []
        
        if not reverse:
            current_node = self._head
            while current_node is not None:
                string_list.append(str(current_node.data))
                current_node = current_node.next
            
        else:
            current_node = self._tail
            while current_node is not None:
                string_list.append(str(current_node.data))
                current_node = current_node.prev
                
        return str(string_list)
        
    def remove(self, target):
        if target >= self._head.data and target <= self._tail.data:
            if target > self._probe.data:
                while self._probe is not None and self._probe.data < target:
                    self._probe = self._probe.next
            else:
                while self._probe is not None and self._probe.data > target:
                    self._probe = self._probe.prev
                    
            if self._probe.data == target:
                if self._probe == self._head:
                    self._head = self._head.next
                    self._head.prev = None
                    
                elif self._probe == self._tail:
                    self._tail = self._tail.prev
                    self._tail.next = None
                
                else:
                    self._probe.prev.next = self._probe.next
                    self._probe.next.prev = self._probe.prev
                    self._probe = self._probe.prev
            
class _DoublyLinkedListNode(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
   
        
def main():
    print("create a DoublyLinkedLIst")
    dlist = DoublyLinkedLIst()
    print("dlist: %s" % dlist.show())
    print()
    print("100 in list? " + str(100 in dlist))
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