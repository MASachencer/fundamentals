from .linkedQueue import LinkedNode
from .linkedQueue import LinkedQueue


class PriorityNode(LinkedNode):
    def __init__(self, data, priority=0):
        LinkedNode.__init__(self, data)
        self.priority = priority


class PriorityQueue(LinkedQueue):
    def __init__(self):
        LinkedQueue.__init__(self)

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
