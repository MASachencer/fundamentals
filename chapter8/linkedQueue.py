class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.head is not None:
            node = self.head
            self.head = node.next
            if self.head is None:
                self.tail = None
            return node.data
        else:
            raise Exception('empty queue')

    def size(self):
        count = 0
        cursor = self.head
        while cursor is not None:
            cursor = cursor.next
            count += 1
        return count

    def iter(self):
        cursor = self.head
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next

    def clear(self):
        self.head = None
        self.tail = None
