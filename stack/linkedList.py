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

    def __getitem__(self, index):
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

    def __contains__(self, item):
        return self.find(item) != -1

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self._size += 1

    def append_head(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp
        if self.head.next is None:
            self.tail = temp
        self._size += 1

    def pop_head(self):
        if self._size > 0:
            temp = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return temp.value
        else:
            raise Exception()

    def pop_tail(self):
        if self._size > 0:
            count = 0
            for node in self.iter_node():
                if count == self._size - 2:
                    temp = node.next
                    node.next = None
                    self.tail = node
                    self._size -= 1
                    return temp.value
        else:
            raise Exception()

    def remove(self, item):
        if item in self:
            if self.head.value == item:
                temp = self.pop_head()
            elif self.tail.value == item:
                temp = self.pop_tail()
            else:
                for node in self.iter_node():
                    if node.next.value == item:
                        node.next = node.next.next
                        self._size -= 1
                        return 1
        else:
            return -1

    # def insert(self, index, item):
    #     if self.head is None or index >= self._size:
    #         self.append(item)
    #     elif index < 1:
    #         self.append_head(item)
    #     else:
    #         count = 0
    #         temp = Node(item)
    #         for node in self.iter_node():
    #             if count == index - 1:
    #                 temp.next = node.next
    #                 node.next = temp
    #                 if temp.next is None:
    #                     self.tail = temp
    #                 self._size += 1
    #                 break
    #             count += 1

    # def pop(self, index):
    #     if index < 1:
    #         self.pop_head()
    #     elif index >= self._size:
    #         self.pop_tail()
    #     else:
    #         count = 0
    #         for node in self.iter_node():
    #             if count == index - 1:
    #                 temp = node.next
    #                 node.next = node.next.next
    #                 if node.next is None:
    #                     self.tail = node
    #                 self._size -= 1
    #                 return temp.value
    #             count += 1
