class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        node = LinkedNode(value)
        node.next = self.top
        self.top = node

    def pop(self):
        node = self.top
        self.top = node.next
        return node.data

    def peek(self):
        return self.top.data

    def size(self):
        count = 0
        cursor = self.top
        while cursor is not None:
            cursor = cursor.next
            count += 1
        return count

    def iter(self):
        cursor = self.top
        while cursor is not None:
            yield cursor.top.data
            cursor = cursor.next

    def clear(self):
        self.top = None
