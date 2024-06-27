from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val: 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def listToBinaryTree(self, values):
        if not values:
            return None
        # Root
        self.root = TreeNode(values[0])
        # Deque for BSF Traversal
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

    def binaryTreeToList(self):
        if not self.root:
            return []
        output = []
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        level = 0
        queue = deque([root, ])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # go to next level
            level += 1
        return levels


if __name__ == '__main__':

    # Inputs and Expected Outputs
    root_1 = [3, 9, 20, None, None, 15, 7]
    expected_output_1 = [[3], [9, 20], [15, 7]]
    root_2 = [1]
    expected_output_2 = [[1]]
    root_3 = []
    expected_output_3 = []

    # Construct Binary Trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    binary_tree_3 = BinaryTree()
    bt_1 = binary_tree_1.listToBinaryTree(root_1)
    bt_2 = binary_tree_2.listToBinaryTree(root_2)
    bt_3 = binary_tree_3.listToBinaryTree(root_3)


    # Print to Test Trees
    tree_1_print_test = binary_tree_1.binaryTreeToList()
    tree_2_print_test = binary_tree_2.binaryTreeToList()
    tree_3_print_test = binary_tree_3.binaryTreeToList()
    print(f"\nTree 1 Print Test: {tree_1_print_test} \nExpected Result: {root_1}")
    print(f"\nTree 2 Print Test: {tree_2_print_test} \nExpected Result: {root_2}")
    print(f"\nTree 3 Print Test: {tree_3_print_test} \nExpected Result: {root_3}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.levelOrder(bt_1)
    test_2 = solution_2.levelOrder(bt_2)
    test_3 = solution_3.levelOrder(bt_3)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3 Result: {test_3} \nExpected Result: {expected_output_3}")