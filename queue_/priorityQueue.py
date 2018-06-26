class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

    def __repr__(self):
        return f'<Node: {self.value}, next: {self.next}>'

class Queue_:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def __iter__(self):
        curr_node = self.front
        while curr_node:
            yield curr_node.value
            curr_node = curr_node.next

    def clear(self, size):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, item):
        temp = Node(item)
        if self.front is None:
            self.front = temp
            self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp
            self._size += 1

    def dequeue(self):
        if self._size > 0:
            temp = self.front
            temp.next = None
            self.front = self.front.next
            return temp.value
        else:
            raise Exception()


class PriorityNode(Node):
    def __init__(self, value, priority=0):
        Node.__init__(self, value)
        self.priority = priority


class PriorityQueue(Queue_):
    def __init__(self):
        Queue_.__init__(self)

    def enqueue(self, item, priority=0):
        node = PriorityNode(item, priority)
        if self.front is None:
            self.front = node
            self.rear = node
        elif node.priority <= self.rear.priority:
            self.rear.next = node
            self.rear = node
        elif node.priority > self.front.priority:
            node.next = self.front
            self.front = node
        else:
            probe = self.front
            while node.priority <= probe.priority:
                trailer = probe
                probe = probe.next
            node.next = probe
            trailer.next = node
