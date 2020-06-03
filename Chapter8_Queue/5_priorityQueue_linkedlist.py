class PriorityQueue(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0
        
    def is_empty(self):
        return self._count == 0
        
    def __len__(self):
        return self._count
        
    def __str__(self):
        current_node = self._head
        string_list = []
        while current_node is not None:
            string_list.append(str((current_node.item, current_node.priority)))
            current_node = current_node.next
        return str(string_list)
        
    def enqueue(self, item, priority):
        new_entry = _PriorityQEntry(item, priority)
        if self.is_empty():
            self._head = new_entry
        else:
            self._tail.next = new_entry
        
        self._tail = new_entry 
        self._count += 1
        
    def dequeue(self):
        assert not self.is_empty(), "cannot pop from empty queue"

        max_priority_entry = self._head
        pre_entry = None

        current_node = self._head
        pre_node = None
        while current_node is not None:
            if current_node.priority > max_priority_entry.priority:
                pre_entry = pre_node
                max_priority_entry = current_node
            
            pre_node = current_node
            current_node = current_node.next
            
        item = max_priority_entry.item
        
        if max_priority_entry == self._head:
            self._head = self._head.next
        else:
            pre_entry.next = max_priority_entry.next
        
        self._count -= 1
        
        return item
        
class _PriorityQEntry(object):
    def __init__(self, item, priority, link=None):
        self.item = item
        self.priority = priority
        self.next = link
        
        
def main():
    print("create new priority")
    Q = PriorityQueue()
    print()
    
    print("add (1,2)")
    Q.enqueue(1,2)
    
    print("add (3,5)")
    Q.enqueue(3,5)
    
    print("add (6,1)")
    Q.enqueue(6,1)
    
    print("add (2,4)")
    Q.enqueue(2,4)
    
    print("add (0,2)")
    Q.enqueue(0,2)
    
    print("add (125,2)")
    Q.enqueue(125,2)
    
    print("add (325,2)")
    Q.enqueue(325,2)
    
    print()
    
    print("Queue: ")
    print(Q)
    
    print("dequeue: %d"% Q.dequeue())
    print(Q)
    print()
        
    print("dequeue: %d"% Q.dequeue())
    print(Q)
    print()
        
    print("dequeue: %d"% Q.dequeue())
    print(Q)
    print()
        
    print("dequeue: %d"% Q.dequeue())
    print(Q)
    print()

    
if __name__ == "__main__":
        main()
    
    
    
    
    
    
    
    
    
    
    