class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None
        
    class Queue:
        def __init__(self):
            self.queue = []
        def enqueue(self, item):
            self.queue.append(item)
        def dequeue(self):
            if not self.is_empty():
                return self.queue.pop(0)
            else:
                return None
        def is_empty(self):
            return len(self.queue) == 0
        def size(self):
            return len(self.queue)
        def peek(self):
            if not self.is_empty():
                return self.queue[0]
            else:
                return None