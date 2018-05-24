class Array:
    def __init__(self, size, fill_value=None):
        self._items = []
        for count in range(size):
            self._items.append(fill_value)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, new_item):
        self._items[index] = new_item


class ArrayBag:
    def __init__(self, source_collection=None):
        self._items = Array(ArrayBag.DEFAULE_CAPACITY)
        self._size = 0
        if source_collection is not None:
            for item in source_collection:
                self.add(item)

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def clear(self):
        self._size = 0
        self._items = Array(ArrayBag.DEFAULE_CAPACITY)

    def add(self, item):
        self._items[len(self)] = item
        self._size += 1

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __str__(self):
        return ', '.join([str(i) for i in self])

    def __add__(self, other):
        result = ArrayBag(self)
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

    def remove(self, item):
        if item not in self:
            raise KeyError(f'{str(item)} not in bag')
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        for i in range(targetIndex, len(self) - 1):
            self._items[i] = self._items[i + 1]
        self._size -= 1
