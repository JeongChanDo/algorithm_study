from queue import LinkedQueue, Node

"""
deque
- 스택과 큐의 결합 ->양쪽에서 조회, 삽입, 삭제 가능
"""
class Deque(LinkedQueue):
    def enqueue_back(self, item):
        node = Node(item)
        self.tail.pointer = node
        self.tail = node
        self.count +=1
    
    def dequeue_front(self):
        if self.tail is not None:
            value = self.tail.value
            node = self.head
            while node:
                if node.pointer.pointer is None:
                    break
                node = node.pointer
            node.pointer = None
            self.tail = node
            self.count -= 1
            return value
        else:
            print("deque is empty")


if __name__ == "__main__":
    deque = Deque()
    print("is dequeu empty? {}".format(deque.isEmpty()))
    print("insert 0 ~ 9 into deque")
    for i in range(10):
        deque.enqueue(i)
    print("size of deque : {}".format(deque.size()))
    print("peek : {}".format(deque.peek()))
    deque.print()
    print("dequeue : {}".format(deque.dequeue()))
    deque.print()
    print("dequeue_front : {}".format(deque.dequeue_front()))
    deque.print()
    print("dequeue_front : {}".format(deque.dequeue_front()))
    deque.print()
    print("enqueue_back(21): {}".format(deque.enqueue_back(21)))
    deque.print()