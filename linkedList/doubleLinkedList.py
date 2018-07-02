from .linkedList import Node, LinkedList

class DoubleNode(Node):
    def __init__(self, value, prev=None, next_=None):
        Node.__init__(value, next_)
        self.prev = prev

    def __repr__(self):
        return f'<Node: {self.value}, prev: {self.prev}, next: {self.next}>'


class DoubleLinkedList(LinkedList):
    def iter_node_reverse(self):
        curr_node = self.tail
        while curr_node:
            yield curr_node.value
            curr_node = curr_node.prev

    def append(self, item):
        temp = DoubleNode(item)
        temp.prev = self.tail
        self.tail = temp
        if self.head is None:
            self.head = temp
        self._size += 1

    def append_head(self, item):
        temp = DoubleNode(item)
        temp.next = self.head
        self.head = temp
        if self.tail is None:
            self.tail = temp
        self._size += 1

    def pop_head(self):
        if self._size > 0:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            if self.head is None:
                self.tail = None
            self._size -= 1
            return temp.value

    def pop_tail(self):
        if self._size > 0:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            if self.tail is None:
                self.head = None
            self._size -= 1
        return temp.value

    def remove(self, item):
        if item in self:
            if self.head.value == item:
                temp = self.pop_head()
            elif self.tail.value == item:
                temp = self.pop_tail()
            else:
                for node in self.iter_node():
                    if node.value == item:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                        self._size -= 1
            return 1
        else:
            return -1
