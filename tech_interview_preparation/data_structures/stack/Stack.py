class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def size(self):
        return len(self.items)


stack = Stack()

print(stack.is_empty())

stack.push(1)
print(stack.items)
stack.push(2)
print(stack.items)
stack.push(3)
print(stack.items)
stack.push(4)
print(stack.items)
stack.push(5)
print(stack.items)

print(stack.is_empty())
print(stack.peek())

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack.is_empty())

print(stack.pop())

print(stack.is_empty())
print(stack.peek())
