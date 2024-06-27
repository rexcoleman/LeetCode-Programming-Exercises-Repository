class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # O(N) linear running time complexity
    def reverse(self):
    # your algorithm goes here !!!
        current_node = self.head
        next_node = None
        prev_node = None
        while current_node:
            next_node = current_node.next_node
            current_node.next_node = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def insert(self, data):

        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def get_head(self):
        return self.head

    def traverse_list(self):

        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next_node

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert(4)
    linked_list.insert(3)
    linked_list.insert(2)
    linked_list.insert(1)
    linked_list.reverse()
    linked_list.traverse_list()

