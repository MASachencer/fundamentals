from ..arrays.array import Array
from ..linkedList.linkedList import LinkedList

class ArrayStack:
    def __init__(self, size=16):
        self._items = Array(size)

    def is_empty(self):
        return self._items.logic() == 0

    def __len__(self):
        return self._items.logic()

    def __iter__(self):
        iter(self._items)

    def clear(self, size):
        self._items = Array(size)

    def push(self, item):
        self._items.append(item)

    def peek(self):
        return self.items[len(self)-1]

    def pop(self):
        return self.items.pop_tail()


class LinkedStack:
    def __init__(self):
        self._items = LinkedList()

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        iter(self._items)

    def clear(self):
        self._items = LinkedList()

    def push(self, item):
        self._items.append(item)

    def peek(self):
        return self.items[len(self)-1]

    def pop(self):
        return self.items.pop_tail()
