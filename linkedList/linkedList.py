class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

    def __repr__(self):
        return f'<Node: {self.value}, next: {self.next}>'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def iter_node(self):
        curr_node = self.head
        while curr_node:
            yield curr_node
            curr_node = curr_node.next

    def __iter__(self):
        for node in self.iter_node():
            yield node.value 

    def index(self, index):
        count = 0
        for item in self:
            if count == index:
                return item

    def find(self, item):
        index = 0
        for target in self:
            if target == item:
                return index
            index += 1
        return -1

    def append(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self._size += 1

    def insert(self, index, item):
        temp = Node(item)
        if self.head is None or index >= self._size:
            self.append(item)
        elif index == 0:
            temp.next = self.head
            self.head = temp
            self._size += 1
        elif 0 < index < self._size:
            count = 0
            for node in self.iter_node():
                if count == index-1:
                    temp.next = node.next
                    node.next = temp
                count += 1
            self._size += 1
        else:
            raise Exception()
        if temp.next is None:
            self.tail = temp

    def remove(self, item):
        if self.find(item) == 1:
            for node in self.iter_node():
                if node.next.value == item:
                    node.next = node.next.next
                    if node.next is None:
                        self.tail = node
                    self._size -= 1
                    return 1
            else:
                return -1

    def pop(self, index):
        if index == 0:
            temp = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return temp.value
        elif 0 < index < self._size:
            count = 0
            for node in self.iter_node():
                if count == index - 1:
                    temp = node.next
                    node.next = node.next.next
                    if node.next is None:
                        self.tail = node
                    self._size -= 1
                    return temp.value
                count += 1
        else:
            raise Exception()

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
