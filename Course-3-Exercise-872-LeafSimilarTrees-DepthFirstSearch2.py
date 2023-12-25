from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def listToBinaryTree(self, values):
        if not values:
            return None
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
            return None
        queue = deque([root])
        while queue:
            current = queue.popleft()
            if current is not None:
                output.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                output.append(None)
        # remove trailing None values
        while output and output[-1] is None:
            output.pop()
        return output


class Solution:

    def leafSimilar(self, root1, root2):
        def dfs(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            return dfs(root.left) + dfs(root.right)

        return dfs(root1) == dfs(root2)

if __name__ == '__main__':

    # Inputs and Expected Outputs
    root1_1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
    root2_1 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
    expected_output_1 = True
    root1_2 = [1, 2, 3]
    root2_2 = [1, 3, 2]
    expected_output_2 = False

    # Construct Binary Trees
    binary_tree_1_1 = BinaryTree()
    binary_tree_2_1 = BinaryTree()
    binary_tree_1_2 = BinaryTree()
    binary_tree_2_2 = BinaryTree()
    bt_1_1 = binary_tree_1_1.listToBinaryTree(root1_1)
    bt_2_1 = binary_tree_2_1.listToBinaryTree(root2_1)
    bt_1_2 = binary_tree_1_2.listToBinaryTree(root1_2)
    bt_2_2 = binary_tree_2_2.listToBinaryTree(root2_2)

    # Print to Test Tree Construction
    print(f"\nTree 1_1 Print Test: {binary_tree_1_1.binaryTreeToList(bt_1_1)} \nExpected Result: {root1_1}")
    print(f"\nTree 2_1 Print Test: {binary_tree_2_1.binaryTreeToList(bt_2_1)} \nExpected Result: {root2_1}")
    print(f"\nTree 1_2 Print Test: {binary_tree_1_2.binaryTreeToList(bt_1_2)} \nExpected Result: {root1_2}")
    print(f"\nTree 2_2 Print Test: {binary_tree_2_2.binaryTreeToList(bt_2_2)} \nExpected Result: {root2_2}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.leafSimilar(bt_1_1, bt_2_1)
    test_2 = solution_2.leafSimilar(bt_2_1, bt_2_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
