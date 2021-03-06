class Stack(object):
    def __init__(self):
        self.items =[]
    
    def isEmpty(self):
        return not bool(self.items)
    
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("stack is empty")
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("stack is empty")
    
    def __repr__(self):
        return repr(self.items)

if __name__ == "__main__":
    stack = Stack()
    print("is stack empty? {}".format(stack.isEmpty))
    print("push 0 ~ 9 to stack")
    for i in range(10):
        stack.push(i)
    print("size of stack : {}".format(stack.size()))
    print("peek : {}". format(stack.peek()))
    print("pop : {}".format(stack.pop()))
    print(stack)