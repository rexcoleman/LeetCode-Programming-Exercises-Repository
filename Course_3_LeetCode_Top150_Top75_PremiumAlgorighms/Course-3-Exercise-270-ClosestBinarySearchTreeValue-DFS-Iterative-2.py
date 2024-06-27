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
        closest = root.val
        while root:
            # Check if current node is closer to the target than the current closest value
            # In case of a tie, prefer the lower value (root.val < closest)
            if abs(root.val - target) < abs(closest - target) or (
                    abs(root.val - target) == abs(closest - target) and root.val < closest):
                closest = root.val

            # Move to the left if target is less than current node's value, otherwise move right
            root = root.left if target < root.val else root.right

        return closest


if __name__ == '__main__':
    # Inputs and Expected Outputs
    root_1 = [4, 2, 5, 1, 3]
    target_1 = 3.714286
    expected_output_1 = 3.5
    root_2 = [1]
    target_2 = 4.428571
    expected_output_2 = 1
    root_3 = [1,None,2]
    target_3 = 3.428571
    expected_output_3 = 2


    # Construct Binary Search Trees
    binarySearchTree_1 = BinarySearchTree()
    binarySearchTree_2 = BinarySearchTree()
    binarySearchTree_3 = BinarySearchTree()
    bst_1 = binarySearchTree_1.listToBinarySearchTree(root_1)
    bst_2 = binarySearchTree_2.listToBinarySearchTree(root_2)
    bst_3 = binarySearchTree_3.listToBinarySearchTree(root_3)

    # Print To Test Tree Construction
    print(f"\nTree 1 Print Test: {binarySearchTree_1.binarySearchTreeToList(bst_1)} \nExpected Output: {root_1}")
    print(f"\nTree 2 Print Test: {binarySearchTree_2.binarySearchTreeToList(bst_2)} \nExpected Output: {root_2}")
    print(f"\nTree 3 Print Test: {binarySearchTree_3.binarySearchTreeToList(bst_3)} \nExpected Output: {root_3}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.closestValue(bst_1, target_1)
    test_2 = solution_2.closestValue(bst_2, target_2)
    test_3 = solution_3.closestValue(bst_3, target_3)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
