class SmallCircularQueue:
    def __init__(self):
        self.capacity = 30
        self.arr = [None] * self.capacity
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, value):
        if self.count == self.capacity:
            raise Exception("Queue full")
        self.arr[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise Exception("Queue empty")
        value = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return value
