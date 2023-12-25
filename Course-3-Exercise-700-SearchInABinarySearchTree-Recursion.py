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
            return []
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

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Search for val
        if not root:
            return None

        def dfs(root):
            if not root:
                return None
            if val == root.val:
                return root
            if val < root.val:
                return dfs(root.left)
            if val > root.val:
                return dfs(root.right)

        return dfs(root)


if __name__ == '__main__':

    # Inputs and Expected Outputs
    root_1 = [4, 2, 7, 1, 3]
    val_1 = 2
    expected_output_1 = [2, 1, 3]
    root_2 = [4, 2, 7, 1, 3]
    val_2 = 5
    expected_output_2 = []

    # Construct Binary Trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    bt_1 = binary_tree_1.listToBinaryTree(root_1)
    bt_2 = binary_tree_2.listToBinaryTree(root_2)

    # Print to Test Tree Construction
    print(f"\nTree 1 Print Test: {binary_tree_1.binaryTreeToList(bt_1)} \nExpected Result: {root_1}")
    print(f"\nTree 2 Print Test: {binary_tree_2.binaryTreeToList(bt_2)} \nExpected Result: {root_1}")


    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.searchBST(bt_1, val_1)
    test_2 = solution_2.searchBST(bt_2, val_2)

    # Print Results
    output_1 = binary_tree_1.binaryTreeToList(test_1)
    output_2 = binary_tree_2.binaryTreeToList(test_2)
    print(f"\nTest 1 Output: {output_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {output_2} \nExpected Output: {expected_output_2}")
