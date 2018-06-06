from linkedQueue import LinkedNode
from linkedQueue import LinkedQueue


class PriorityQueue(LinkedQueue):
    def __init__(self):
        LinkedQueue.__init__(self)

    def enqueue(self, item):
        if self.front is None or item >= self.rear.data:
            LinkedQueue.enqueue(self, item)
        else:
            probe = self.front
            while item >= probe.data:
                trailer = probe
                probe = probe.next
            node = LinkedNode(item)
            node.next = probe
            if probe == self.front:
                self.front = node
            else:
                trailer.next = node
