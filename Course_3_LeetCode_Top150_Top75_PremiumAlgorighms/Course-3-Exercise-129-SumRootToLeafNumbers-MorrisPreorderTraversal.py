from typing import Optional
from collections import deque


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
        # Set the root as the first element of the values list
        self.root = TreeNode(values[0])
        # Use deque to track nodes in breadth first search traversal
        queue = deque([self.root])
        i = 1
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

    def binaryTreeToList(self, root):
        if not root:
            return []
        output = []
        # Use deque to track nodes with breadth first search traversal
        queue = deque([root])
        while queue:
            current = queue.popleft()
            if current is not None:
                output.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                output.append(None)
        # Remove trailing None values
        while output and output[-1] is None:
            output.pop()
        return output


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        root_to_leaf = curr_number = 0

        while root:
            # If there is a left child, then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left:
                # Predecessor node is one step to the left
                # and then to the right till you can.
                predecessor = root.left
                steps = 1
                while predecessor.right and predecessor.right is not root:
                    predecessor = predecessor.right
                    steps += 1
                # Set link predecessor.right = root and go to explore the left subtree
                if predecessor.right is None:
                    curr_number = curr_number * 10 + root.val
                    predecessor.right = root
                    root = root.left
                # Break the link predecessor.right = root. Once the link is broken,
                # it's time to change subtree and go to the right
                else:
                    # If you're on the leaf, update the sum
                    if predecessor.left is None:
                        root_to_leaf += curr_number
                    # This part of tree is explored, backtrack
                    for _ in range(steps):
                        curr_number //= 10
                    predecessor.right = None
                    root = root.right

            # If there is no left child then just go right.
            else:
                curr_number = curr_number * 10 + root.val
                # if you're on the leaf, update the sum
                if root.right is None:
                    root_to_leaf += curr_number
                root = root.right
        return root_to_leaf




if __name__ == "__main__":

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

    # Print to test trees
    print_test_1 = binary_tree_1.binaryTreeToList(bt_1)
    print_test_2 = binary_tree_2.binaryTreeToList(bt_2)
    print(f"\nBinary Tree Print Test 1: {print_test_1} \nExpected Result: {root_1}")
    print(f"\nBinary Tree Print Test 2: {print_test_2} \nExpected Result: {root_2}")

    # Run tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.sumNumbers(bt_1)
    test_2 = solution_2.sumNumbers(bt_2)

    # Print results
    print(f"\nResult 1: {test_1}\nExpected Result: {expected_output_1}")
    print(f"\nResult 2: {test_2}\nExpected Result: {expected_output_2}")