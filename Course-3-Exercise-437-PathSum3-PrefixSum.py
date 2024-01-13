from collections import deque, defaultdict
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
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def preorder(node: TreeNode, curr_sum) -> None:
            nonlocal count
            if not node:
                return

                # The current prefix sum
            curr_sum += node.val

            # Here is the sum we're looking for
            if curr_sum == k:
                count += 1

            # The number of times the curr_sum − k has occurred already,
            # determines the number of times a path with sum k
            # has occurred up to the current node
            count += h[curr_sum - k]

            # Add the current sum into a hashmap
            # to use it during the child nodes' processing
            h[curr_sum] += 1

            # Process the left subtree
            preorder(node.left, curr_sum)
            # Process the right subtree
            preorder(node.right, curr_sum)

            # Remove the current sum from the hashmap
            # in order not to use it during
            # the parallel subtree processing
            h[curr_sum] -= 1

        count, k = 0, targetSum
        h = defaultdict(int)
        preorder(root, 0)
        return count



if __name__ == '__main__':

    # Inputs and Expected Outputs:
    root_1 = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    targetSum_1 = 8
    expected_output_1 = 3
    root_2 = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    targetSum_2 = 22
    expected_output_2 = 3
    root_3 = []
    targetSum_3 = 1
    expected_output_3 = 0
    root_4 = [1]
    targetSum_4 = 0
    expected_output_4 = 0
    root_5 = [0,1,1]
    targetSum_5 = 1
    expected_output_5 = 4


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
    bt_5 = binary_tree_5.listToBinaryTree(root_5)

    # Print To Test Tree Construction
    print(f"\nTree 1 Print Test {binary_tree_1.binaryTreeToList(bt_1)} \nExpected Output: {root_1}")
    print(f"\nTree 2 Print Test {binary_tree_2.binaryTreeToList(bt_2)} \nExpected Output: {root_2}")
    print(f"\nTree 3 Print Test {binary_tree_3.binaryTreeToList(bt_3)} \nExpected Output: {root_3}")
    print(f"\nTree 4 Print Test {binary_tree_4.binaryTreeToList(bt_4)} \nExpected Output: {root_4}")
    print(f"\nTree 5 Print Test {binary_tree_5.binaryTreeToList(bt_5)} \nExpected Output: {root_5}")

    # Run Test
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    solution_5 = Solution()
    test_1 = solution_1.pathSum(bt_1, targetSum_1)
    test_2 = solution_2.pathSum(bt_2, targetSum_2)
    test_3 = solution_3.pathSum(bt_3, targetSum_3)
    test_4 = solution_4.pathSum(bt_4, targetSum_4)
    test_5 = solution_5.pathSum(bt_5, targetSum_5)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
    print(f"\nTest 4 Output: {test_4} \nExpected Output: {expected_output_4}")
    print(f"\nTest 5 Output: {test_5} \nExpected Output: {expected_output_5}")
