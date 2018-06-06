class LinkedNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


node1 = None
node2 = LinkedNode('A', None)
node3 = LinkedNode('B', node2)
node1 = LinkedNode('C', node3)
node1 = LinkedNode('C', None)
node1.next = node3
head0 = node1

head1 = None
for count in range(1, 6):
    head1 = LinkedNode(count, head1)

lyst = [1, 2, 3, 4, 5]
head2 = None
for count in lyst[::-1]:
    head2 = LinkedNode(count, head2)


def iter(head):
    probe = head
    while probe is not None:
        yield probe.data
        probe = probe.next


for i in iter(head0):
    print(i)


def search(head, item):
    probe = head
    while probe is not None and item != probe.data:
        probe = probe.next
    if probe is not None:
        return True
    else:
        return False


def index(head, index):
    probe = head
    while index > 0:
        probe = probe.index
        index -= 1
    return probe.data


def replace_item(head, item, new):
    probe = head
    while probe is not None and item != probe.data:
        probe = probe.next
    if probe is not None:
        probe.data = new
    else:
        raise ValueError


def replace_index(head, index, new):
    probe = head
    while index > 0:
        probe = probe.next
        index -= 1
    probe.data = new


def insert_head(head, item):
    head = LinkedNode(item, head)


def insert_tail(head, item):
    new = item
    if head is None:
        head = new
    else:
        probe = head
        while probe.next is not None:
            probe = probe.next
        probe.next = new
    head = probe


def remove_head(head):
    item = head.data
    head = head.next
    return item


def remove_tail(head):
    item = head.data
    if head.next is None:
        head = None
    else:
        probe = head
        while probe.next is not None:
            probe = probe.next
        item = probe.next.data
        probe.next = None
    return item


def insert(head, index, item):
    if head is None or index < 1:
        head = LinkedNode(item, head)
    else:
        probe = head
        while index > 1 and probe.next is not None:
            probe = probe.next
            index -= 1
    probe.next = LinkedNode(item, probe.next)


def remove(head, index):
    if index < 1 or head.next is None:
        item = head.data
        head = head.next
        return item
    else:
        probe = head
    while index > 1 and probe.next.next is not None:
        probe = probe.next
        index -= 1
    item = probe.next.data
    probe.next = probe.next.next
    return item
