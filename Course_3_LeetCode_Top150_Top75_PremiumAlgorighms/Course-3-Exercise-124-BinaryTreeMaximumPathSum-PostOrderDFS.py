from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def listToBinaryTree(self, values):
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        i = 1
        while i < len(values):
            current = queue.popleft()
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1
        return self.root


    def binaryTreeToList(self, root):
        output = []
        if not root:
            return output
        queue = deque([root])
        while queue:
            current = queue.popleft()
            if current is not None:
                output.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                output.append(None)
        while output and output[-1] is None:
            output.pop()
        return output


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = -float('inf')

        # post order traversal of subtree rooted at `node`
        def gain_from_subtree(node: Optional[TreeNode]) -> int:
            nonlocal max_path

            if not node:
                return 0

            # add the gain from the left subtree. Note that if the gain is negative, we can ignore it,
            # or count it as 0. This is the reason we use `max` here.
            gain_from_left = max(gain_from_subtree(node.left), 0)

            # add the gain / path sum from right subtree. 0 if negative
            gain_from_right = max(gain_from_subtree(node.right), 0)

            # if left or right gain are negative, they are counted
            # as 0, so this statement takes care of all four scenarios
            max_path = max(max_path, gain_from_left + gain_from_right + node.val)

            # return the max sum for a path starting at the root of subtree
            return max(gain_from_left + node.val, gain_from_right + node.val)

        gain_from_subtree(root)
        return max_path


if __name__ == '__main__':

    # Inputs and Expected Outputs
    root_1 = [1, 2, 3]
    expected_output_1 = 6
    root_2 = [-10, 9, 20, None, None, 15, 7]
    expected_output_2 = 42

    # Construct Binary Trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    bt_1 = binary_tree_1.listToBinaryTree(root_1)
    bt_2 = binary_tree_2.listToBinaryTree(root_2)

    # Print to Test Binary Trees
    tree_1_print_test = binary_tree_1.binaryTreeToList(bt_1)
    tree_2_print_test = binary_tree_2.binaryTreeToList(bt_2)
    print(f"\nTree 1 Print Test: {tree_1_print_test} \nExpected Result: {root_1}")
    print(f"\nTree 2 Print Test: {tree_2_print_test} \nExpected Result: {root_2}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.maxPathSum(bt_1)
    test_2 = solution_2.maxPathSum(bt_2)

    # Print Results
    output_1 = binary_tree_1.binaryTreeToList(bt_1)
    output_2 = binary_tree_2.binaryTreeToList(bt_2)
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")

