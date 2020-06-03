from myarray import Array
from linkedlistqueue import Queue

class BoundedPriorityQueue(object):
    def __init__(self, num_levels):
        self._qlist = Array(num_levels)
        self._num_levels = num_levels
        self._count = 0
        
        for i in range(num_levels):
            self._qlist[i] = Queue()
            
    def __str__(self):
        string_list = []
        for i in range(self._num_levels):
            string_list.append(str(self._qlist[i]))
        return str(string_list)
        
    def is_empty(self):
        return self._count == 0
        
    def __len__(self):
        return self._count
        
    def enqueue(self, item, priority):
        assert priority >=0 and priority < self._num_levels, "invalid priority"
        self._qlist[priority].enqueue(item)
        self._count += 1
        
    def dequeue(self):
        assert not self.is_empty(), "cannot pop from empty queue"
        i = self._num_levels - 1
        while i >=0 and self._qlist[i].is_empty():
            i -=1
        self._count -= 1
        return self._qlist[i].dequeue()
        
        
def main():
    print("create new priority")
    Q = BoundedPriorityQueue(5)
    print()
    
    print("add (1,1)")
    Q.enqueue(1,1)
    
    print("add (165,0)")
    Q.enqueue(165,0)
    
    print("add (15,0)")
    Q.enqueue(15,0)
    
    print("add (3,2)")
    Q.enqueue(3,2)
    
    print("add (6,3)")
    Q.enqueue(6,3)
    
    print("add (2,4)")
    Q.enqueue(2,4)
    
    print("add (0,3)")
    Q.enqueue(0,3)
    
    print("add (125,4)")
    Q.enqueue(125,4)
    
    print("add (325,2)")
    Q.enqueue(325,2)
    
    print()
    
    print("Queue: ")
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
        
    print("dequeue: %d"% Q.dequeue())
    print(Q)
    print()

    
if __name__ == "__main__":
        main()