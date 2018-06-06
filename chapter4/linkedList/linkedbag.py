from linkedNode import LinkedNode


class LinkedBag:
    def __init__(self, sourceCollection=None):
        self._items = None
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __iter__(self):
        cursor = self._items
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next

    def add(self, item):
        self._items = LinkedNode(item, self._items)
        self._size += 1

    def isEmpty(self):
        return self._items is None

    def insert(self, index, item):
        pass

    def remove(self, index):
        return

    def search(self, target):
        cursor = self.head
        while cursor is not None and cursor.data != target:
            cursor = cursor.next
        return cursor is not None

    # def remove(self, item):
    #     if item not in self:
    #         raise KeyError(f'{str(item)} not in bag')
    #     probe = self._items
    #     trailer = None
    #     for target in self:
    #         if target == item:
    #             break
    #         trailer = probe
    #         probe = probe.next
    #     if probe == self._items:
    #         self._items = self._items.next
    #     else:
    #         trailer.next = probe.next
    #     self._size -= 1
