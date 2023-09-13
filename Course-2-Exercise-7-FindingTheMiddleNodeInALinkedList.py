
class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # O(N) linear running time complexity
    def get_middle_node(self):
    # your implementation goes here !!!
        slow_node = self.head
        fast_node = self.head
        while fast_node.next_node and fast_node.next_node.next_node:
            fast_node = fast_node.next_node.next_node
            slow_node = slow_node.next_node
        # print("%d" % slow_node.data)
        return slow_node

    def insert(self, data):

        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def traverse_list(self):

        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next_node


class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

if __name__ == '__main__':
    linked_list = LinkedList()
    # linked_list.insert(5)
    linked_list.insert(4)
    linked_list.insert(3)
    linked_list.insert(2)
    linked_list.insert(1)
    # linked_list.get_middle_node()
    print(linked_list.get_middle_node().data)