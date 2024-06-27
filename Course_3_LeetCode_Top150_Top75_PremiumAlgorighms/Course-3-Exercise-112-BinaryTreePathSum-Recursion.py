from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def list_to_binary_tree(self, values):
        if not values:
            return None
        # Create root node from first value
        self.root = TreeNode(values[0])
        # Use deque to keep track of tree nodes
        queue = deque([self.root])
        i = 1
        # Iterate through values to build tree
        while i < len(values):
            current = queue.popleft()
            # Left node
            if i < len(values) and values[i]:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            # Right node
            if i < len(values) and values[i]:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1
        return self.root

    def print_tree(self):
        if not self.root:
            return
        # Use deque to keep track of nodes
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            print(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

class Solution:
    def has_path_sum(self, root, sum):
        if not root:
            return False
        sum -= root.val
        # Test for leaf
        if not root.left and not root.right:
            return sum == 0
        return self.has_path_sum(root.left, sum) or \
            self.has_path_sum(root.right, sum)


if __name__ == '__main__':

    # Inputs
    root1 = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    targetSum1 = 22
    root2 = [1, 2, 3]
    targetSum2 = 5
    root3 = []
    targetSum3 = 0

    # Construct Binary Trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    binary_tree_3 = BinaryTree()

    bt_1 = binary_tree_1.list_to_binary_tree(root1)
    bt_2 = binary_tree_2.list_to_binary_tree(root2)
    bt_3 = binary_tree_3.list_to_binary_tree(root3)

    # Print to test tree construction
    print(f"Tree 1 Print Test:")
    binary_tree_1.print_tree()
    print(f"Tree 2 Print Test:")
    binary_tree_2.print_tree()
    print(f"Tree 3 Print Test:")
    binary_tree_3.print_tree()

    # Test path sum
    solution = Solution()

    test_1 = solution.has_path_sum(bt_1, targetSum1)
    test_2 = solution.has_path_sum(bt_2, targetSum2)
    test_3 = solution.has_path_sum(bt_3, targetSum3)

    print(f"Output 1: {test_1}")
    print(f"Output 2: {test_2}")
    print(f"Output 3: {test_3}")
