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
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque([(root, float("-inf"))])
        num_good_nodes = 0
        while queue:
            node, max_so_far = queue.popleft()
            if max_so_far <= node.val:
                num_good_nodes += 1
            if node.right:
                queue.append((node.right, max(node.val, max_so_far)))
            if node.left:
                queue.append((node.left, max(node.val, max_so_far)))

        return num_good_nodes


if __name__ == '__main__':
    # Inputs and Expected Outputs
    root_1 = [3, 1, 4, 3, None, 1, 5]
    expected_output_1 = 4
    root_2 = [3, 3, None, 4, 2]
    expected_output_2 = 3
    root_3 = [1]
    expected_output_3 = 1
    root_4 = [9, None, 3, 6]
    expected_output_4 = 1

    # Construct Binary trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    binary_tree_3 = BinaryTree()
    binary_tree_4 = BinaryTree()
    bt_1 = binary_tree_1.listToBinaryTree(root_1)
    bt_2 = binary_tree_2.listToBinaryTree(root_2)
    bt_3 = binary_tree_3.listToBinaryTree(root_3)
    bt_4 = binary_tree_4.listToBinaryTree(root_4)

    # Print to Test Tree Construction
    print(f"\nTree 1 Print Test: {binary_tree_1.binaryTreeToList(bt_1)} \nExpected Output: {root_1}")
    print(f"\nTree 2 Print Test: {binary_tree_2.binaryTreeToList(bt_2)} \nExpected Output: {root_2}")
    print(f"\nTree 3 Print Test: {binary_tree_3.binaryTreeToList(bt_3)} \nExpected Output: {root_3}")
    print(f"\nTree 4 Print Test: {binary_tree_4.binaryTreeToList(bt_4)} \nExpected Output: {root_4}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    test_1 = solution_1.goodNodes(bt_1)
    test_2 = solution_2.goodNodes(bt_2)
    test_3 = solution_3.goodNodes(bt_3)
    test_4 = solution_4.goodNodes(bt_4)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \n Expected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \n Expected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \n Expected Output: {expected_output_3}")
    print(f"\nTest 4 Output: {test_4} \n Expected Output: {expected_output_4}")

