class Queue:
    def __init__(self):
        self.queue = []
        self.stack = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if self.empty():
            return None
        if len(self.stack) == 0:
            while len(self.queue) > 0:
                self.stack.append(self.queue.pop())
        return self.stack.pop()

    def peek(self):
        if self.empty():
            return None
        if len(self.stack) == 0:
            while len(self.queue) > 0:
                self.stack.append(self.queue.pop())
        return self.stack[-1]

    def empty(self):
        return len(self.queue) == 0 and len(self.stack) == 0


q = Queue()
print(q.empty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())

q.enqueue(4)
print(q.dequeue())
print(q.peek())
print(q.empty())
print(q.dequeue())
print(q.empty())
