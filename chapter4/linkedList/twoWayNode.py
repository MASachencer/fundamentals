from linkedNode import LinkedNode


class TwoWayNode(LinkedNode):
    def __init__(self, data, previous=None, next=None):
        LinkedNode.__init__(self, data, next)
        self.previous = previous


head = TwoWayNode(1)
tail = head
for data in range(2, 6):
    tail.next = TwoWayNode(data, tail)
    tail = tail.next

probe = tail
while probe is not None:
    print(probe.data)
    probe = probe.previous
