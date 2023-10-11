from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def list_to_binary_tree(self, values):
        if not values:
            return None
        # Create root node with first element of values
        self.root = TreeNode(values[0])
        # Use a deque to keep track of nodes
        queue = deque([self.root])
        i = 1
        # Iterate through values to add tree nodes (BFS)
        while i < len(values):
            current = queue.popleft()
            # Left node
            if i < len(values) and values[i]:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            # Right node
            if i < len(values) and values[i]:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1
        return self.root

    def print_tree(self):
        if not self.root:
            return
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            print(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

class Solution:

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return
        queue = deque([root])
        answer = []
        while queue:
            queue_len = len(queue)
            row = 0
            for i in range(queue_len):
                node = queue.popleft()
                row += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            answer.append(row/queue_len)
            print(f"answer {answer}")
        return answer




if __name__ == '__main__':

    # Inputs
    root1 = [3, 9, 20, None, None, 15, 7]
    root2 = [3, 9, 20, 15, 7]
    root3 = []

    # Construct Trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    binary_tree_3 = BinaryTree()

    bt_1 = binary_tree_1.list_to_binary_tree(root1)
    bt_2 = binary_tree_2.list_to_binary_tree(root2)
    bt_3 = binary_tree_3.list_to_binary_tree(root3)

    # Print to test tree construction
    print("Print tree 1:")
    binary_tree_1.print_tree()
    print("Print tree 2:")
    binary_tree_2.print_tree()
    print("Print tree 3:")
    binary_tree_3.print_tree()

    # Compute average for each level
    solution = Solution()

    test_1 = solution.averageOfLevels(bt_1)
    test_2 = solution.averageOfLevels(bt_2)
    test_3 = solution.averageOfLevels(bt_3)

    print(f"Test 1 Output: {test_1}")
    print(f"Test 2 Output: {test_2}")
    print(f"Test 3 Output: {test_3}")