class Queue(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return not bool(self.items)
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("queue is empty")
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("queue is empty")
    
    def __repr__(self):
        return repr(self.items)

if __name__ == "__main__":
    queue = Queue()
    print("is queue empty ? {}".format(queue.isEmpty()))
    print("insert 0 ~ 9 into queue")
    for i in range(10):
        queue.enqueue(i)
    print("size of queue : {}".format(queue.size()))
    print(queue)
    print("peek : {}".format(queue.peek()))
    print("dequeue : {}".format(queue.dequeue()))
    print("peek : {}".format(queue.peek()))
    print("is queue empty? : {}".format(queue.isEmpty()))
    print(queue)
