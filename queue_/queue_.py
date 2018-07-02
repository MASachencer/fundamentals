from array import Array
from linkedList import LinkedList


class ArrayQueue:
    def __init__(self, size=16):
        self._items = Array(size=16)

    def is_empty(self):
        return self._items.logic() == 0

    def __len__(self):
        return self._items.logic()

    def __iter__(self):
        iter(self._items)

    def clear(self, size):
        self._items = Array(size)

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)


class LinkedQueue:
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

    def enqueue(self, item):
        self._items.append(item)        

    def dequeue(self):
        return self._items.pop_head()
