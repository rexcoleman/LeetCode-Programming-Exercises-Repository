from collections import deque
from typing import Optional, List


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
        queue = deque([self.root])
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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node:TreeNode, level: int, sum_at_current_level: List) -> None:
            if not node:
                return
            if len(sum_at_current_level) == level:
                sum_at_current_level.append(node.val)
            else:
                sum_at_current_level[level] += node.val

            dfs(node.left, level + 1, sum_at_current_level)
            dfs(node.right, level + 1, sum_at_current_level)


        sum_at_current_level = []
        dfs(root, 0, sum_at_current_level)
        return 1 + sum_at_current_level.index(max(sum_at_current_level))



if __name__ == '__main__':

    # Inputs and Expected Outputs
    root_1 = [1, 7, 0, 7, -8, None, None]
    expected_output_1 = 2
    root_2 = [989, None, 10250, 98693, -89388, None, None, None, -32127]
    expected_output_2 = 2

    # Construct Binary Trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    bt_1 = binary_tree_1.listToBinaryTree(root_1)
    bt_2 = binary_tree_2.listToBinaryTree(root_2)

    # Print To Test Tree Construction
    print(f"\nTree 1 Print Test: {binary_tree_1.binaryTreeToList(bt_1)} \nExpected Output: {root_1}")
    print(f"\nTree 2 Print Test: {binary_tree_2.binaryTreeToList(bt_2)} \nExpected Output: {root_2}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.maxLevelSum(bt_1)
    test_2 = solution_2.maxLevelSum(bt_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 1 Output: {test_2} \nExpected Output: {expected_output_2}")
