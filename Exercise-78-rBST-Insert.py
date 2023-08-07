class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)



    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)


my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

"""
    THE LINES ABOVE CREATE THIS TREE:
                 2
                / \
               1   3
"""

print('Root:', my_tree.root.value)
print('Root -> Left:', my_tree.root.left.value)
print('Root -> Right:', my_tree.root.right.value)

"""
    EXPECTED OUTPUT:
    ----------------
	Root: 2
	Root -> Left: 1
	Root -> Right: 3

"""

