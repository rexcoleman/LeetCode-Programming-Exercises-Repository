class Node:

    def __init__(self, data, parent):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.height = 0


class AVLTree:

    def __init__(self):
        # we can access the root node exclusively
        self.root = None

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # we have to consider the left subtree
        if data < node.data:
            # we have to check if the left node is none
            # when the left child is not none
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
        # we have to consider the right subtree
        else:
            # we have to check if the right node is none
            # when the right child is not none
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1

        # After every insertion we have to check if the AVL properties are violated
        self.handle_violation(node)

    def remove_node(self, data, node):

        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:
            # we have found the node we want to remove
            # case 1: if the node is a leaf node
            if node.left_node is None and node.right_node is None:
                print('Removing a leaf node...%d' %node.data)
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None
                if parent is None:
                    self.root = None

                del node

                # After every insertion we have to check if the AVL properties are violated
                self.handle_violation(parent)

            # case 2: if the node has a single right child
            elif node.left_node is None and node.right_node is not None:
                print('Removing a node with a single right child...%d' %node.data)
                parent = node.parent
                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.right_node
                    if parent is not None:
                        if parent.right_node == node:
                            parent.right_node = node.right_node
                else:
                    self.root = node.right_node

                node.right_node.parent = parent
                del node

                # After every insertion we have to check if the AVL properties are violated
                self.handle_violation(parent)

            # case 3: if the node has a single left child
            elif node.right_node is None and node.left_node is not None:
                print('Removing a node with a single left child...%d' %node.data)
                parent = node.parent
                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent is not None:
                        if parent.right_node == node:
                            parent.right_node = node.left_node
                else:
                    self.root = node.left_node

                node.left_node.parent = parent
                del node
                # After every insertion we have to check if the AVL properties are violated
                self.handle_violation(parent)
            # case 4: the node has two children
            else:
                print('Removing a node with two children...%d')
                predecessor = self.get_predecessor(node.left_node)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)
        return node

    def handle_violation(self, node):
        # check the nodes from the node we have inserted up to the root node
        while node is not None:
            node.height = max(self.calc_height(node.left_node),
                              self.calc_height(node.right_node)) + 1
            self.violation_helper(node)
            # whenever we settle a violation (rotations) it may happen that it
            # violates the AVL properties in other parts of the tree
            node = node.parent

    # checks if the subtree is balanced with the root tree = node
    def violation_helper(self, node):
        balance = self.calculate_balance(node)
        # OK, the tree is left heavy but it can be left-right heavy or left-left heavy
        if balance > 1:
            # left-right heavy situation: left rotation on parent + right rotation on grandparent
            if self.calculate_balance(node.left_node) < 0:
                self.rotate_left(node.left_node)
            # this is the right rotation of the grandparent (if left-left heavy, that's a simple right rotation)
            self.rotate_right(node)
        # OK, the tree is right heavy but it can be right-right heavy or right-left heavy
        if balance < -1:
            # right-left heavy situation: we need a right rotation on parent before left rotation on grandparent
            if self.calculate_balance(node.right_node) > 0:
                self.rotate_right(node.right_node)
            # this is the left rotation of the grandparent
            self.rotate_left(node)


    def calc_height(self, node):
        # this is when the node is a Null
        if node is None:
            return -1
        return node.height

    def calculate_balance(self, node):
        if node is None:
            return 0
        return self.calc_height(node.left_node) - self.calc_height(node.right_node)

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)

        l = ''
        r = ''
        p = ''

        if node.left_node is not None:
            l = node.left_node.data
        else:
            l = 'NULL'

        if node.right_node is not None:
            r = node.right_node.data
        else:
            r = 'NULL'

        if node.parent is not None:
            p = node.parent.data
        else:
            p = 'NULL'

        print('%s left: %s right: %s parent: %s height: %s' % (node.data, l, r, p, node.height))

        if node.right_node:
            self.traverse_in_order(node.right_node)



    def rotate_right(self, node):
        print('Rotating to the right on node ', node.data)

        temp_left_node = node.left_node
        t = temp_left_node.right_node

        temp_left_node.right_node = node
        node.left_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.left_node == node:
            temp_left_node.parent.left_node = temp_left_node
        if temp_left_node.parent is not None and temp_left_node.parent.right_node == node:
            temp_left_node.parent.right_node = temp_left_node
        if node == self.root:
            self.root = temp_left_node

        node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
        temp_left_node.height = max(self.calc_height(temp_left_node.left_node),
                                    self.calc_height(temp_left_node.right_node)) + 1

    def rotate_left(self, node):
        print('Rotating to the left on node ', node.data)

        temp_right_node = node.right_node
        t = temp_right_node.left_node

        temp_right_node.left_node = node
        node.right_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None and temp_right_node.parent.left_node == node:
            temp_right_node.parent.left_node = temp_right_node
        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_right_node.parent.right_node = temp_right_node
        if node == self.root:
            self.root = temp_right_node

        node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
        temp_right_node.height = max(self.calc_height(temp_right_node.left_node),
                                    self.calc_height(temp_right_node.right_node)) + 1


if __name__ == '__main__':

    avl = AVLTree()
    avl.insert(5)
    avl.insert(3)
    avl.insert(10)
    avl.insert(2)
    avl.insert(4)
    avl.insert(15)
    avl.remove(15)
    avl.remove(10)

    #
    # avl.insert(32)
    # avl.insert(16)
    # avl.insert(48)
    # avl.insert(8)
    # avl.insert(24)
    # avl.insert(40)
    # avl.insert(56)
    # avl.insert(36)
    # avl.insert(44)
    # avl.insert(52)
    # avl.insert(60)
    # avl.insert(4)
    # avl.insert(58)
    # avl.insert(62)
    # avl.remove(4)
    #
    # avl.traverse()