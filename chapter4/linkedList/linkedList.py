from linkedNode import LinkedNode


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self._size == 0

    def append(self, item):
        temp = LinkedNode(item)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

    def insert(self, index, item):
        temp = LinkedNode(item)
        if self.head is None or index < 1:
            temp.next = self.head
            self.head = temp
        else:
            cursor = self.head
            while index > 1 and cursor.next is not None:
                cursor = cursor.next
                index -= 1
            temp.next = cursor.next
            cursor.next = temp
        if temp.next is None:
            self.tail = temp

    def remove(self, index):
        if index < 1 or self.head.next is None:
            item = self.head.data
            if self.head.next is None:
                self.tail = None
            self.head = self.head.next
        else:
            cursor = self.head
            while index > 1 and cursor.next is not None:
                cursor = cursor.next
                index -= 1
            item = cursor.next.data
            cursor.next = cursor.next.next
            if cursor.next is None:
                self.tail = cursor
        return item

    def search(self, target):
        cursor = self.head
        while cursor is not None and cursor.data != target:
            cursor = cursor.next
        return cursor is not None

    def iter(self):
        cursor = self.head
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next

    def size(self):
        cursor = self.head
        count = 0
        while cursor is not None:
            count += 1
            cursor = cursor.next
        return count


if __name__ == '__main__':
    pass
