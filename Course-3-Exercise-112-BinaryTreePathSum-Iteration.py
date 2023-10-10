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
        # Create root node with first element of values
        self.root = TreeNode(values[0])
        # Use deque to keep track of binary tree nodes
        queue = deque([self.root])
        i = 1
        # Iterate through values to add nodes to binary tree (BFS)
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
        # Iterate through nodes (BFS)
        while queue:
            current = queue.popleft()
            print(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        de = [(root, sum - root.val), ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            # Start with node.right because we are using a stack
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        # If we get to the end of the loop return False
        return False


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

    # Test for tree path sum
    solution = Solution()

    test_1 = solution.hasPathSum(bt_1, targetSum1)
    test_2 = solution.hasPathSum(bt_2, targetSum2)
    test_3 = solution.hasPathSum(bt_3, targetSum3)

    print(f"Output 1: {test_1}")
    print(f"Output 2: {test_2}")
    print(f"Output 3: {test_3}")