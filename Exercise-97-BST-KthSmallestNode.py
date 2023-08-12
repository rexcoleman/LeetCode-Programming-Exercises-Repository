class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # def kth_smallest(self, k):
    #     print(f"k = {k}")
    #     # create a stack to hold nodes
    #     stack = []
    #     # start at the root of the tree
    #     temp = self.root
    #     print(f"temp at initialization {temp}")
    #
    #     while stack or temp:
    #         # traverse to the leftmost node
    #         while temp:
    #             print(f"k = {k}")
    #             # add the node to the stack
    #             stack.append(temp)
    #             temp = temp.left
    #             print(f"temp_while-inner {temp}")
    #         # pop the last node added to the stack
    #         temp = stack.pop()
    #         print(f"temp_ {temp.value}")
    #         k -= 1
    #         # if kth smallest element is found, return the value
    #         if k == 0:
    #             return temp.value
    #         # move to the right child of the node
    #         temp = temp.right
    #         print(f"temp {temp}")
    #         # if k is greater than the number of nodes in the tree, return None
    #     return None

    def kth_smallest(self, k):
        self.kth_smallest_count = 0
        return self.kth_smallest_helper(self.root, k)

    def kth_smallest_helper(self, node, k):
        # print(node)
        print(self.kth_smallest_count)
        if node is None:
            return None

        left_result = self.kth_smallest_helper(node.left, k)
        if left_result is not None:
            return left_result

        self.kth_smallest_count += 1
        if self.kth_smallest_count == k:
            return node.value

        right_result = self.kth_smallest_helper(node.right, k)
        if right_result is not None:
            return right_result

        return None


bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# print(bst.kth_smallest(1))  # Expected output: 2
# print(bst.kth_smallest(3))  # Expected output: 4
print(bst.kth_smallest(6))  # Expected output: 7

"""
    EXPECTED OUTPUT:
    ----------------
    2
    4
    7

 """