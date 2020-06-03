class PriorityQueue(object):
    def __init__(self):
        self._qlist = list()
        
    def is_empty(self):
        return len(self._qlist) == 0
        
    def __len__(self):
        return len(self._qlist)
        
    def __str__(self):
        string_list = [ str((entry.item, entry.priority)) for entry in self._qlist]
        return str(string_list)
        
    def enqueue(self, item, priority):
        new_entry = _PriorityQEntry(item, priority)
        self._qlist.append(new_entry)
        
    def dequeue(self):
        assert not self.is_empty(), "cannot pop from empty queue"
        
        priority_max = self._qlist[0].priority
        idx = 0
        for i in range(len(self)):
            if self._qlist[i].priority > priority_max:
                priority_max = self._qlist[i].priority
                idx = i
        
        return self._qlist.pop(idx).item
        
class _PriorityQEntry(object):
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        
        
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
    
    
    
    
    
    
    
    
    
    
    