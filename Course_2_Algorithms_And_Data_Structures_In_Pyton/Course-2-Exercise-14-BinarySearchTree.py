class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        # when implementing the remove function
        self.parent = parent


class BinarySearchTree:

    def __init__(self):
        # we can access the root node exclusively
        self.root = None

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def insert(self, data):
        # this is the first node in the BST
        if self.root is None:
            self.root = Node(data)
        # the BST is not empty
        else:
            self.insert_node(data, self.root)

    def remove_node(self, data, node):
        # first we have to find the node we want to remove
        if node is None:
            return
        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:
            # we have found the node we want to remove
            # there are 3 options
            # LEAF NODE CASE
            if node.left_node is None and node.right_node is None:
                print('Removing a leaf node...%d' % node.data)
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None
                if parent is None:
                    self.root = None
                del node

            # WHEN THERE IS A SINGLE CHILD
            elif node.left_node is None and node.right_node is not None:
                print('Removing a node with a single right child...')
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = node.right_node
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.right_node
                if parent is None:
                    self.root = node.right_node
                node.right_node.parent = parent
                del node

            elif node.right_node is None and node.left_node is not None:
                print('Removing a node with a single left child...')
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = node.left_node
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.left_node
                if parent is None:
                    self.root = node.left_node
                node.left_node.parent = parent

            # REMOVE NODE WITH TWO CHILDREN
            else:
                print('Removing a node with two children...')
                predecessor = self.get_predecessor(node.left_node)

                # swap the node and the predecessor
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                self.remove_node(data, predecessor)


    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)
        return node


    def insert_node(self, data, node):
        # we have to go to the left subtree
        if data < node.data:
            if node.left_node:
                # the left node exists (so we keep going)
                self.insert_node(data, node.left_node)
            else:
                # there is no left child (so we create one)
                node.left_node = Node(data, node)
        # we have to go to the right subtree
        else:
            if node.right_node:
                # the right node exists (so we keep going)
                self.insert_node(data, node.right_node)
            else:
                # there is no right child (so we create one)
                node.right_node = Node(data, node)

    def get_min(self):
        if self.root:
            return self.get_min_value(self.root)

    def get_min_value(self, node):
        if node.left_node:
            return self.get_min_value(node.left_node)
        return node.data

    def get_max(self):
        if self.root:
            return self.get_max_value(self.root)

    def get_max_value(self, node):
        if node.right_node:
            return self.get_max_value(node.right_node)
        return node.data

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    # it has O(N) linear running time complexity
    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)
        print(node.data)

        if node.right_node:
            self.traverse_in_order(node.right_node)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(8)
    bst.insert(12)
    bst.insert(-5)
    bst.remove(10)
    bst.remove(5)
    bst.remove(8)
    bst.remove(-5)
    bst.remove(12)

    print('Max value: %s' % bst.get_max())
    print('Min value: %s' % bst.get_min())
    bst.traverse()
