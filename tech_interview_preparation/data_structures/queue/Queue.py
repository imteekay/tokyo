class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return self.size() == 0

    def front(self):
        if not self.is_empty():
            return self.items[0]

    def back(self):
        if not self.is_empty():
            return self.items[self.size() - 1]

    def size(self):
        return len(self.items)


def test_emptiness(queue):
    is_empty = queue.is_empty()
    print(is_empty)


def test_size(queue):
    size = queue.size()
    print(size)


def test_front(queue):
    front = queue.front()
    print(front)


def test_back(queue):
    back = queue.back()
    print(back)


queue = Queue()

test_emptiness(queue)
test_size(queue)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

test_emptiness(queue)
test_size(queue)
test_front(queue)
test_back(queue)

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()

test_emptiness(queue)
test_size(queue)
test_front(queue)
test_back(queue)

queue.dequeue()

test_emptiness(queue)
test_size(queue)
test_front(queue)
test_back(queue)
