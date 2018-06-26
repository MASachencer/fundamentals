from ..arrays.array import Array
from ..linkedList.linkedList import LinkedList


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

    def add_front(self, item):
        self._items.insert(0, item)

    def add_rear(self, item):
        self._items.append(item)

    def remove_front(self):
        return self._items.pop(0)

    def remove_rear(self):
        return self._items.pop(len(self)-1)


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

    def add_front(self, item):
        self._items.append_head(item)

    def add_rear(self, item):
        self._items.append(item)

    def remove_front(self):
        return self._items.pop_head()

    def remove_rear(self):
        return self._items.pop_tail()
