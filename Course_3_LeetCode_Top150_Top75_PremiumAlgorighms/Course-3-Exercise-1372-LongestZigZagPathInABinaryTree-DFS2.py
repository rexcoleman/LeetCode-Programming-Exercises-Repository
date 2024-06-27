from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right = None):
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
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.pathLength = 0
        def dfs(node, goLeft, steps):
            if node:
                self.pathLength = max(self.pathLength, steps)
                if goLeft:
                    dfs(node.left, False, steps + 1)
                    dfs(node.right, True, 1)
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, steps + 1)


        dfs(root, False, 0)
        dfs(root, True, 0)
        return self.pathLength



if __name__ == '__main__':

    # Inputs and Expected Outputs
    root_1 = [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]
    expected_output_1 = 3
    root_2 = [1, 1, 1, None, 1, None, None, 1, 1, None, 1]
    expected_output_2 = 4
    root_3 = [1]
    expected_output_3 = 0
    root_4 = [1, None, 1, 1, 1, None, None, None, 1]
    expected_output_4 = 2

    # Construct Binary Trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    binary_tree_3 = BinaryTree()
    binary_tree_4 = BinaryTree()
    bt_1 = binary_tree_1.listToBinaryTree(root_1)
    bt_2 = binary_tree_2.listToBinaryTree(root_2)
    bt_3 = binary_tree_3.listToBinaryTree(root_3)
    bt_4 = binary_tree_4.listToBinaryTree(root_4)

    # Print To Test Tree Construction
    print(f"\nBinary Tree 1 Print Test: {binary_tree_1.binaryTreeToList(bt_1)} \nExpected Output: {root_1}")
    print(f"\nBinary Tree 2 Print Test: {binary_tree_2.binaryTreeToList(bt_2)} \nExpected Output: {root_2}")
    print(f"\nBinary Tree 3 Print Test: {binary_tree_3.binaryTreeToList(bt_3)} \nExpected Output: {root_3}")
    print(f"\nBinary Tree 4 Print Test: {binary_tree_4.binaryTreeToList(bt_4)} \nExpected Output: {root_4}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    test_1 = solution_1.longestZigZag(bt_1)
    test_2 = solution_2.longestZigZag(bt_2)
    test_3 = solution_3.longestZigZag(bt_3)
    test_4 = solution_4.longestZigZag(bt_4)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
    print(f"\nTest 4 Output: {test_4} \nExpected Output: {expected_output_4}")