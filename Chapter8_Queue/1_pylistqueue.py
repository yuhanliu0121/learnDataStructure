class Queue(object):
    def __init__(self):
        self._queue_list = list()
        
    def is_empty(self):
        return len(self._queue_list) == 0
        
    def __len__(self):
        return len(self._queue_list)
        
    def enqueue(self, item):
        self._queue_list.append(item)
        
    def dequeue(self):
        assert not self.is_empty(), "cannot dequeue from empty queue"
        return self._queue_list.pop(0)
        
    def __str__(self):
        return str(self._queue_list)
        
def main():
    print("create a queue")
    Q = Queue()
    
    print("add 1 to the queue")
    Q.enqueue(1)
    print(Q)
    print()
    
    print("add 2 to the queue")
    Q.enqueue(2)
    print(Q)
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
    
if __name__ == "__main__":
    main()
    