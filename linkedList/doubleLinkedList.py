from .linkedList import Node, LinkedList

class DoubleNode(Node):
    def __init__(self, value, prev=None, next_=None):
        Node.__init__(value, next_)
        self.prev = prev

    def __repr__(self):
        return f'<Node: {self.value}, prev: {self.prve}, next: {self.next}>'


class DoubleLinkedList(LinkedList):
    def iter_node_reverse(self):
        curr_node = self.tail
        while curr_node:
            yield curr_node.value
            curr_node = curr_node.prev

    def append(self, item):
        temp = DoubleNode(item)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            temp.prev = self.tail
            self.tail.next = temp
            self.tail = temp
        self._size += 1

    def insert(self, index, item):
        pass

    def remove(self, item):
        return

    def pop(self, index):
        return
