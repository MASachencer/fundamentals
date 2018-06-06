class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        node = LinkedNode(item)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is not None:
            node = self.front
            self.front = node.next
            if self.front is None:
                self.rear = None
            return node.data
        else:
            raise Exception('empty queue')

    def size(self):
        count = 0
        cursor = self.front
        while cursor is not None:
            cursor = cursor.next
            count += 1
        return count

    def iter(self):
        cursor = self.front
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next

    def clear(self):
        self.front = None
        self.rear = None
