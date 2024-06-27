import math
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


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

    def binaryTreeToList(self, queue):
        output = []
        if not self.root:
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
        # Remove trailing None values
        while output and output[-1] == None:
            output.pop()
        return output


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return (validate(node.right, node.val, high) and
                    validate(node.left, low, node.val))
        return validate(root)





if __name__ == '__main__':
    # Inputs and Expected Outputs
    root_1 = [2,1,3]
    expected_output_1 = True
    root_2 = [5,1,4,None,None,3,6]
    expected_output_2 = False

    # Construct Binary Trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    bt_1 = binary_tree_1.listToBinaryTree(root_1)
    bt_2 = binary_tree_2.listToBinaryTree(root_2)

    # Print to Test Binary Tree Construction
    tree_1_print = binary_tree_1.binaryTreeToList(bt_1)
    tree_2_print = binary_tree_2.binaryTreeToList(bt_2)
    print(f"\nTree 1 Print Test: {tree_1_print} \nExpected Result: {root_1}")
    print(f"\nTree 2 Print Test: {tree_2_print} \nExpected Result: {root_2}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.isValidBST(bt_1)
    test_2 = solution_2.isValidBST(bt_2)


    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
