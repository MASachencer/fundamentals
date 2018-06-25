from ..arrays.array import Array
from ..linkedList.linkedList import LinkedList


class ArrayQueue:
    pass

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
        self._items.append_head(item)        

    def dequeue(self):
        return self._items.pop_tail()
