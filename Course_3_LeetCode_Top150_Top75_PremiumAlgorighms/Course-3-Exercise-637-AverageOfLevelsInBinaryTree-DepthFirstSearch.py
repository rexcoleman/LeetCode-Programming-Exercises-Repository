from collections import deque, defaultdict
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
        # Use deque to keep track of binary tree nodes
        queue = deque([self.root])
        i = 1
        # Iterate through values and add nodes to tree
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
        # Use deque to keep track of nodes
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
        lvlcnt = defaultdict(int)
        lvlsum = defaultdict(int)
        print(f"lvlcnt {lvlcnt}")
        print(f"lvlsum {lvlsum}")

        def dfs(node=root, level=0):
            if not node: return
            lvlcnt[level] += 1
            lvlsum[level] += node.val
            print(f"lvlcnt {lvlcnt}")
            print(f"lvlsum {lvlsum}")
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs()
        return [lvlsum[i] / lvlcnt[i] for i in range(len(lvlcnt))]


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

    solution = Solution()

    test_1 = solution.averageOfLevels(bt_1)
    test_2 = solution.averageOfLevels(bt_2)
    test_3 = solution.averageOfLevels(bt_3)

    print(f"Result 1: {test_1}")
    print(f"Result 2: {test_2}")
    print(f"Result 2: {test_3}")


