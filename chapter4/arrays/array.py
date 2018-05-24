class Array:
    def __init__(self, size=0, fill_value=None):
        self._items = []
        self._size = size
        for count in range(size):
            self._items.append(fill_value)

    def __len__(self):
        count = 0
        for i in self._items:
            count += 1
        return count

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __getitem__(self, index):
        return self[index]

    def __setitem__(self, index, new_item):
        self._items[index] = new_item

    def add(self, item):
        self._items[len(self)] = item
        self._size += 1

    def __add__(self, other):
        result = self
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if item not in other:
                return False
        return True

    def is_empty(self):
        return len(self) == 0

    def clear(self):
        self._size = 0
        self._items = []

    def remove(self, item):
        if item not in self._items:
            raise KeyError
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        for i in range(targetIndex, len(self) - 1):
            self._items[i] = self._items[i + 1]
        self._size -= 1
