#
# Minimal ring buffer implementation
#

class RingBuffer:

    def __init__(self, size):
        self.size = size
        self.buffer = {}
        self.head = 0
        self.tail = 0
        self.length = 0

        self.clear()

    def put(self, item):
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % len(self.buffer)

        if self.length == len(self.buffer):
            self.head = self.tail
        else:
            self.length += 1

    def get(self):
        result = self.buffer[self.head]

        self.head = (self.head + 1) % len(self.buffer)
        self.length -= 1

        return result

    def clear(self):
        self.tail = 0
        self.head = 0
        self.length = 0

        for i in range(self.size):
            self.buffer[i] = None
            
    def isempty(self):
        if self.length == 0:
            return 1

        return 0

    def isfull(self):
        if self.length == len(self.buffer):
            return 1

        return 0
