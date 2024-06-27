from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def listToBinarySearchTree(self, values):
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

    def binarySearchTreeToList(self, root):
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
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        stack, pred = [], float('-inf')

        while stack or root:
            while root:
                a = root.val
                stack.append(root)
                root = root.left
            root = stack.pop()
            b = root.val

            if pred <= target and target < root.val:
                return min(pred, root.val, key=lambda x: abs(target - x))

            pred = root.val
            root = root.right

        return pred


if __name__ == '__main__':
    # Inputs and Expected Outputs
    root_1 = [4, 2, 5, 1, 3]
    target_1 = 3.714286
    expected_output_1 = 4
    root_2 = [1]
    target_2 = 4.428571
    expected_output_2 = 1

    # Construct Binary Search Trees
    binarySearchTree_1 = BinarySearchTree()
    binarySearchTree_2 = BinarySearchTree()
    bst_1 = binarySearchTree_1.listToBinarySearchTree(root_1)
    bst_2 = binarySearchTree_2.listToBinarySearchTree(root_2)

    # Print To Test Tree Construction
    print(f"\nTree 1 Print Test: {binarySearchTree_1.binarySearchTreeToList(bst_1)} \nExpected Output: {root_1}")
    print(f"\nTree 2 Print Test: {binarySearchTree_2.binarySearchTreeToList(bst_2)} \nExpected Output: {root_2}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.closestValue(bst_1, target_1)
    test_2 = solution_2.closestValue(bst_2, target_2)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")