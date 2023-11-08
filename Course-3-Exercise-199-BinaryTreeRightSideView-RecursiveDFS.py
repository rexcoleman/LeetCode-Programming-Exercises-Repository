from collections import deque
from typing import Optional, List


class TreeNone:
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
        # Construct root with 1'st element of values list
        self.root = TreeNone(values[0])
        # Use deque to track nodes using breadth first search traversal
        queue = deque([self.root])
        i = 1
        while i < len(values):
            current = queue.popleft()
            # Left child
            if i < len(values) and values[i] is not None:
                current.left = TreeNone(values[i])
                queue.append(current.left)
            i += 1
            # Right child
            if i < len(values) and values[i] is not None:
                current.right = TreeNone(values[i])
                queue.append(current.right)
            i += 1
        return self.root

    def binaryTreeToList(self):
        if not self.root:
            return []
        output = []
        # Use deque to traverse tree using breadth first search
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
        while output and output[-1] is None:
            output.pop()
        return output

class Solution:
    def rightSideView(self, root: Optional[TreeNone]) -> List[int]:
        if not root:
            return []
        rightside = []

        def helper(node: TreeNone, level: int) -> None:
            if level == len(rightside):
                rightside.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    helper(child, level + 1)

        helper(root, 0)
        return rightside





if __name__ == '__main__':

    # Inputs and Expected Outputs
    root_1 = [1, 2, 3, None, 5, None, 4]
    expected_output_1 = [1, 3, 4]
    root_2 = [1, None, 3]
    expected_output_2 = [1, 3]
    root_3 = []
    expected_output_3 = []

    # Construct binary trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    binary_tree_3 = BinaryTree()
    bt_1 = binary_tree_1.listToBinaryTree(root_1)
    bt_2 = binary_tree_2.listToBinaryTree(root_2)
    bt_3 = binary_tree_3.listToBinaryTree(root_3)

    # Print to test tree construction
    tree_1_print_test = binary_tree_1.binaryTreeToList()
    tree_2_print_test = binary_tree_2.binaryTreeToList()
    tree_3_print_test = binary_tree_3.binaryTreeToList()
    print(f"\nTree 1 Print Test: {tree_1_print_test} \nExpected Result: {root_1}")
    print(f"\nTree 2 Print Test: {tree_2_print_test} \nExpected Result: {root_2}")
    print(f"\nTree 3 Print Test: {tree_3_print_test} \nExpected Result: {root_3}")

    # Run tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.rightSideView(bt_1)
    test_2 = solution_2.rightSideView(bt_2)
    test_3 = solution_3.rightSideView(bt_3)

    # Print results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3 Result: {test_3} \nExpected Result: {expected_output_3}")