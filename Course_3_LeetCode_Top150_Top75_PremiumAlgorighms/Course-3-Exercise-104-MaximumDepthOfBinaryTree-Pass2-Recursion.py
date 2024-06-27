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
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        i = 1
        while i < len(values):
            current = queue.popleft()
            if values[i] and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            if values[i] and values[i] is not None:
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

        # Remove Trailing None Values
        while output and output[-1] is None:
            output.pop()
        return output


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(root):
            if root is None:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            return max(left_height, right_height) + 1

        return dfs(root)




if __name__ == '__main__':

    # Inputs and Expected Outputs
    root_1 = [3, 9, 20, None, None, 15, 7]
    expected_output_1 = 3
    root_2 = [1, None, 2]
    expected_output_2 = 2

    # Construct Binary Trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    bt_1 = binary_tree_1.listToBinaryTree(root_1)
    bt_2 = binary_tree_2.listToBinaryTree(root_2)

    # Print to Test Tree Construction
    print(f"\nTree 1 Print Test: {binary_tree_1.binaryTreeToList(bt_1)} \nExpected Result: {root_1}")
    print(f"\nTree 2 Print Test: {binary_tree_2.binaryTreeToList(bt_2)} \nExpected Result: {root_2}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.maxDepth(bt_1)
    test_2 = solution_2.maxDepth(bt_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")


