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

    # Construct tree using breadth first search method
    def listToBinaryTree(self, values):
        if not values:
            return None
        self.root = TreeNode(values[0])
        # Use deque to track nodes
        queue = deque([self.root])
        i = 1
        # Iterate though list to add nodes
        while i < len(values):
            current = queue.popleft()
            # Left node
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            # Right node
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1
        return self.root

    # Construct list from binary tree using breadth first search method
    def binaryTreeToList(self, root):
        if not self.root:
            return []
        output = []
        # Use deque for BFS node tracking
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if current:
                output.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                output.append(None)
        # Remove trailing None values
        while output and output[-1] == None:
            output.pop()
        return output


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        root_to_leaf = 0
        stack = [(root, 0)]

        while stack:
            root, curr_number = stack.pop()
            if root is not None:
                curr_number = curr_number * 10 + root.val
                # if it's a leaf, update root-to-leaf sum
                if root.left is None and root.right is None:
                    root_to_leaf += curr_number
                else:
                    stack.append((root.right, curr_number))
                    stack.append((root.left, curr_number))
        return root_to_leaf



if __name__ == '__main__':

    # Inputs and Expected Outputs
    root_1 = [1, 2, 3]
    expected_output_1 = 25
    root_2 = [4, 9, 0, 5, 1]
    expected_output_2 = 1026

    # Construct binary trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    bt_1 = binary_tree_1.listToBinaryTree(root_1)
    bt_2 = binary_tree_2.listToBinaryTree(root_2)

    # Print to test binary trees
    print_tree_1 = binary_tree_1.binaryTreeToList(bt_1)
    print_tree_2 = binary_tree_2.binaryTreeToList(bt_2)
    print(f"\nPrint Test 1: {print_tree_1} \nExpected Result: {root_1}")
    print(f"\nPrint Test 2: {print_tree_2} \nExpected Result: {root_2}")

    # Run tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.sumNumbers(bt_1)
    test_2 = solution_2.sumNumbers(bt_2)

    # Print results
    print(f"\nResult 1: {test_1}\nExpected Result: {expected_output_1}")
    print(f"\nResult 2: {test_2}\nExpected Result: {expected_output_2}")