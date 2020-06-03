class Queue(object):

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
        temp_list = []
        
        while current_node is not None:
            temp_list.append(current_node.item)
            current_node = current_node.next
        return str(temp_list)
        
    def enqueue(self, item):
        new_node = _QueueNode(item)
        
        if self.is_empty():
            self._head = new_node
            self._tail = self._head
            
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._count +=1
            
    def dequeue(self):
        assert not self.is_empty(), "cannot pop from empty queue"
        temp = self._head.item
        self._head = self._head.next
        self._count -=1
        return temp
        
        
class _QueueNode(object):
    def __init__(self, item, link=None):
        self.item = item
        self.next = link
        
def main():
    print("create a queue")
    Q = Queue()
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
    
if __name__ == "__main__":
    main()