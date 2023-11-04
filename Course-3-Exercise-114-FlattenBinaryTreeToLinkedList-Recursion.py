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
        # Use deque to keep track of nodes
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
        output = []
        if not root:
            return []
        # Use deque to keep track of nodes
        queue = deque([root])
        while queue:
            current = queue.popleft()
            if current:
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

    def flattenTree(self, node):
        # Handle the null scenario
        if not node:
            return None
        # For a leaf node, we simply return the node as is.
        if not node.left and not node.right:
            return node
        # Recursively flatten the left subtree
        leftTail = self.flattenTree(node.left)
        # Recursively flatten the right subtree
        rightTail = self.flattenTree(node.right)

        # If there was a left subtree, we shuffle the connections
        # around so that there is nothing on the left side anymore.
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None

        # We need to return the "rightmost" node after we are
        # done wiring the new connections.
        return rightTail if rightTail else leftTail

    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None
        self.flattenTree(root)




if __name__ == '__main__':

    # Inputs
    root_1 = [1, 2, 5, 3, 4, None, 6]
    expected_output_1 = [1,None,2,None,3,None,4,None,5,None,6]
    root_2 = []
    expected_output_2 = []
    root_3 = [0]
    expected_output_3 = [0]

    # Construct binary trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    binary_tree_3 = BinaryTree()
    bt_1 = binary_tree_1.listToBinaryTree(root_1)
    bt_2 = binary_tree_2.listToBinaryTree(root_2)
    bt_3 = binary_tree_3.listToBinaryTree(root_3)

    # Print to test binary trees
    print(f"\nPrint Test 1: {binary_tree_1.binaryTreeToList(bt_1)}"
          f"\nExpected Result: {root_1}")
    print(f"\nPrint Test 2: {binary_tree_2.binaryTreeToList(bt_2)}"
          f"\nExpected Result: {root_2}")
    print(f"\nPrint Test 3: {binary_tree_3.binaryTreeToList(bt_3)}"
          f"\nExpected Result: {root_3}")

    # Run tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.flatten(bt_1)
    test_2 = solution_2.flatten(bt_2)
    test_3 = solution_3.flatten(bt_3)

    # Access and print the flattened binary trees
    result_1 = binary_tree_1.binaryTreeToList(bt_1)
    result_2 = binary_tree_2.binaryTreeToList(bt_2)
    result_3 = binary_tree_3.binaryTreeToList(bt_3)

    print(f"\nFlattened Tree 1: {result_1}\nExpected Result: {expected_output_1}")
    print(f"\nFlattened Tree 2: {result_2}\nExpected Result: {expected_output_2}")
    print(f"\nFlattened Tree 3: {result_3}\nExpected Result: {expected_output_3}")




    # print(test_1.val)