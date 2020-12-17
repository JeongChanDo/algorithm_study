class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = None
    
class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def enqueue(self, item):
        node = Node(item)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            if self.tail:
                self.tail.pointer = node
            self.tail = node
        self.count +=1
    
    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            self.count -= 1
            return value
        else:
            print("queue is empty")
    
    def print(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()
    
    def size(self):
        return self.count
    
    def peek(self):
        return self.head.value
    
    def isEmpty(self):
        return not bool(self.head)

if __name__ == "__main__":
    queue = LinkedQueue()
    print("is queue empty ? : {}".format(queue.isEmpty()))
    print("push 0 ~ 9 into queue")
    for i in range(0, 10):
        queue.enqueue(i)
    print("is queue empty? : {}".format(queue.isEmpty()))
    print("peek : {}".format(queue.peek()))
    print("size of queue : {}".format(queue.size()))
    queue.print()
    print("dequeue : {}".format(queue.dequeue()))
    queue.print()
    print("size of queue : {}".format(queue.size()))
    queue.print()
    print("dequeue : {}".format(queue.dequeue()))
    queue.print()
    print("dequeue : {}".format(queue.dequeue()))
    queue.print()
    print("dequeue : {}".format(queue.dequeue()))