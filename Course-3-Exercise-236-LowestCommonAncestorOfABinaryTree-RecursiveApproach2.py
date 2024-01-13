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
        self.p_node = None
        self.q_node = None

    def inputNodeAssignment(self, node, p, q):
        if node.val == p:
            self.p_node = node
            print(f"Found P Node: {self.p_node.val}")
            return self.p_node
        if node.val == q:
            self.q_node = node
            print(f"Found q Node: {self.q_node.val}")
            return self.q_node

    def listToBinaryTree(self, values, p, q):
        if not values or not p or not q:
            return None
        self.root = TreeNode(values[0])
        if self.root.val == p or self.root.val == q:
            self.inputNodeAssignment(self.root, p, q)
        queue = deque([self.root])
        i = 1
        while i < len(values):
            current = queue.popleft()
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                if current.left.val == p or current.left.val == q:
                    self.inputNodeAssignment(current.left, p, q)
                queue.append(current.left)
            i += 1
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                if current.right.val == p or current.right.val == q:
                    self.inputNodeAssignment(current.right, p, q)
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

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p: Optional[TreeNode], q: Optional[TreeNode]):

        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False
            b = current_node.val
            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node
                a = self.ans.val

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans


if __name__ == '__main__':

    # Inputs and Expected Outputs
    root_1 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p_1 = 5
    q_1 = 1
    expected_output_1 = 3
    root_2 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p_2 = 5
    q_2 = 4
    expected_output_2 = 5
    root_3 = [1, 2]
    p_3 = 1
    q_3 = 2
    expected_output_3 = 1

    # Construct Binary Trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    binary_tree_3 = BinaryTree()
    bt_1 = binary_tree_1.listToBinaryTree(root_1, p_1, q_1)
    bt_2 = binary_tree_2.listToBinaryTree(root_2, p_2, q_2)
    bt_3 = binary_tree_3.listToBinaryTree(root_3, p_3, q_3)

    # Print To Test Tree Construction
    print(f"\nBinary Tree 1 Print Test: {binary_tree_1.binaryTreeToList(bt_1)} \nExpected Output: {root_1}")
    print(f"\nBinary Tree 2 Print Test: {binary_tree_2.binaryTreeToList(bt_2)} \nExpected Output: {root_2}")
    print(f"\nBinary Tree 3 Print Test: {binary_tree_3.binaryTreeToList(bt_3)} \nExpected Output: {root_3}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.lowestCommonAncestor(bt_1, binary_tree_1.p_node, binary_tree_1.q_node)
    test_2 = solution_2.lowestCommonAncestor(bt_2, binary_tree_2.p_node, binary_tree_2.q_node)
    test_3 = solution_3.lowestCommonAncestor(bt_3, binary_tree_3.p_node, binary_tree_3.q_node)

    # Print Results
    print(f"\nTest 1 Output: {test_1.val} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2.val} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3.val} \nExpected Output: {expected_output_3}")
