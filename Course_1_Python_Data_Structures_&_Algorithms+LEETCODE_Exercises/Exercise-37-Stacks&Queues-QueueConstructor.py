class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1


my_queue = Queue(4)

print('First:', my_queue.first.value)
print('Last:', my_queue.last.value)
print('Length:', my_queue.length)

"""
    EXPECTED OUTPUT:
    ----------------
    First: 4
    Last: 4
    Length: 1

"""