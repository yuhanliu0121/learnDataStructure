from myarray import Array

class Queue(object):
    
    def __init__(self, max_size):
        self._queue = Array(max_size)
        self._count = 0
        self._front = 0
        self._back = max_size - 1
        self._max_size = max_size
        
    def is_empty(self):
        return self._count == 0
        
    def is_full(self):
        return self._count == len(self._queue)
        
    def __len__(self):
        return len(self._queue)
        
    def __str__(self):
        string_list = [str(i) + ',' for i in self._queue]
        return ''.join(string_list)
        
    def enqueue(self, item):
        assert not self.is_full(), "queue is full"
        self._back = (self._back + 1) % self._max_size
        self._queue[self._back] = item
        self._count += 1
        
    def dequeue(self):
        assert not self.is_empty(), "queue is empty"
        temp = self._queue[self._front]
     #   self._queue[self._front] = None
        self._front = (self._front + 1) % self._max_size
        self._count -= 1
        return temp
        
def main():
    print("create a queue")
    Q = Queue(5)
    print("count: %d" % Q._count)
    
    print("add 1 to the queue")
    Q.enqueue(1)
    print(Q)
    print("count: %d" % Q._count)
    print()
    
    print("add 2 to the queue")
    Q.enqueue(2)
    print(Q)
    print("count: %d" % Q._count)
    print()
    
    print("add 4 to the queue")
    Q.enqueue(4)
    print(Q)
    print()
    
    print("add 6 to the queue")
    Q.enqueue(6)
    print(Q)
    print()
    
    print("add 7 to the queue")
    Q.enqueue(7)
    print(Q)
    print()
    
    print("dequeue : %f" % Q.dequeue())
    print(Q)
    print()
    
    print("dequeue: %f" % Q.dequeue())
    print(Q)
    print()
    
    print("add 71 to the queue")
    Q.enqueue(71)
    print(Q)
    print()
    
    print("add 27 to the queue")
    Q.enqueue(27)
    print(Q)
    print()
    
    print("dequeue: %f" % Q.dequeue())
    print(Q)
    print()
    
    print("dequeue: %f" % Q.dequeue())
    print(Q)
    print()
    
if __name__ == "__main__":
    main()
        