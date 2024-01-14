from collections import deque
from typing import List, Optional


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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        right_side = []

        def helper(node: TreeNode, level: int) -> None:
            if level == len(right_side):
                right_side.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    helper(child, level + 1)
        helper(root, 0)
        return right_side



if __name__ == '__main__':

    # Inputs and Expected Outputs
    root_1 = [1, 2, 3, None, 5, None, 4]
    expected_output_1 = [1, 3, 4]
    root_2 = [1, None, 3]
    expected_output_2 = [1, 3]
    root_3 = []
    expected_output_3 = []
    root_4 = [1, 2]
    expected_output_4 = [1,2]
    root_5 = [1, 2, 3, 4]
    expected_output_5 = [1, 3, 4]

    # Construct Binary Trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    binary_tree_3 = BinaryTree()
    binary_tree_4 = BinaryTree()
    binary_tree_5 = BinaryTree()
    bt_1 = binary_tree_1.listToBinaryTree(root_1)
    bt_2 = binary_tree_2.listToBinaryTree(root_2)
    bt_3 = binary_tree_3.listToBinaryTree(root_3)
    bt_4 = binary_tree_4.listToBinaryTree(root_4)
    bt_5= binary_tree_5.listToBinaryTree(root_5)

    # Print To Test Binary Tree Construction
    print(f"\nBinary Tree 1 Print Test: {binary_tree_1.binaryTreeToList(bt_1)} \nExpected Output: {root_1}")
    print(f"\nBinary Tree 2 Print Test: {binary_tree_2.binaryTreeToList(bt_2)} \nExpected Output: {root_2}")
    print(f"\nBinary Tree 3 Print Test: {binary_tree_3.binaryTreeToList(bt_3)} \nExpected Output: {root_3}")
    print(f"\nBinary Tree 4 Print Test: {binary_tree_4.binaryTreeToList(bt_4)} \nExpected Output: {root_4}")
    print(f"\nBinary Tree 5 Print Test: {binary_tree_5.binaryTreeToList(bt_5)} \nExpected Output: {root_5}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    solution_5 = Solution()
    test_1 = solution_1.rightSideView(bt_1)
    test_2 = solution_2.rightSideView(bt_2)
    test_3 = solution_3.rightSideView(bt_3)
    test_4 = solution_4.rightSideView(bt_4)
    test_5 = solution_5.rightSideView(bt_5)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
    print(f"\nTest 4 Output: {test_4} \nExpected Output: {expected_output_4}")
    print(f"\nTest 5 Output: {test_5} \nExpected Output: {expected_output_5}")