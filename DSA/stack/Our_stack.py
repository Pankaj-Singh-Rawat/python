class Our_stack:

    def __init__(self):
        self.stack = []
        self.size = -1

    def push(self, num):
        self.size += 1
        self.stack.append(num)

    def pop(self):
        print(self.stack[self.size - 1])
        self.size -= 1

    def peek(self):
        print(self.stack[self.size - 1])

    def isEmpty(self):
        if self.size == -1:
            print("Stack is empty")

    def size1(self):
        print(self.size + 1)

stack = Our_stack()
stack.push(5)
stack.size1()
stack.peek()
stack.pop()
stack.isEmpty()
