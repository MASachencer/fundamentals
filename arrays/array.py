class Array:
    def __init__(self, size=16, value=None):
        self._size = size
        self._items = [value] * size
        self._logic = 0
        
    def is_empty(self):
        return self._logic == 0

    def __len__(self):
        return self._size

    def logic(self):
        return self._logic

    def __iter__(self):
        index = 0
        while index < self._logic:
            yield self._items[index]
            index += 1

    def __getitem__(self, index):
        if 0 <= index < self._logic:
            return self._items[index]
        else:
            raise Exception()

    def __setitem__(self, index, new_item):
        if 0 <= index < self._logic:
            self._items[index] = new_item
        else:
            raise Exception()

    def __contains__(self, item):
        for target in self:
            if target == item:
                return True
        return False

    def append(self, item):
        if self._logic < self._size:
            self._items[self._logic] = item
            self._logic += 1
        else:
            raise Exception()

    def insert(self, index, item):
        if self._logic < self._size:
            while index < self._size:
                self._items[index], item = item, self._items[index+1]
                index += 1
            self._logic += 1
        else:
            raise Exception()

    def remove(self, item):
        if item in self._items:
            self._items.remove(item)
            self._logic -= 1
        else:
            raise Exception()

    def pop(self, index):
        target = self._items[index]
        if target:
            self.remove(target)
            self._logic -= 1
            return target
        else:
            raise Exception()

    def __add__(self, other):
        if isinstance(other, type(self)):
            result = self
            for target in other:
                result.append(target)
            return result

    def __eq__(self, other):
        if self is other:
            return True
        if isinstance(other, type(self)) or self.logic() != other.logic():
            return False
        for item in self:
            if item not in other:
                return False
        return True

    def clear(self, value=None):
        for i in range(self._size):
            self._items[i] = value
        self._logic = 0
