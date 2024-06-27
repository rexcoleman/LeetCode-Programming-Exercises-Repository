from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def list_to_binary_search_tree(self, values):
        if not values:
            return None
        # Create root node with first element of values
        self.root = TreeNode(values[0])
        # Use a deque to keep track of nodes
        queue = deque([self.root])
        i = 1
        # Iterate through list to add nodes to tree (BFS)
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

    def print_tree(self):
        if not self.root:
            return None
        # Use a deque to keep track of tree nodes (BFS)
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            print(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nodeValues = []

        def dfs(node):
            if node is None:
                return
            nodeValues.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        nodeValues.sort()
        minDifference = 1e9
        for i in range(1, len(nodeValues)):
            minDifference = min(minDifference, nodeValues[i] - nodeValues[i - 1])
            print(f"minDifference {minDifference}")
        return minDifference



if __name__ == '__main__':

    # Inputs
    root1 = [4, 2, 6, 1, 3]
    root2 = [1, 7, 48, None, None, 12, 69]

    # Construct binary search trees
    binary_search_tree_1 = BinarySearchTree()
    binary_search_tree_2 = BinarySearchTree()


    bst_1 = binary_search_tree_1.list_to_binary_search_tree(root1)
    bst_2 = binary_search_tree_2.list_to_binary_search_tree(root2)

    # Print to test tree construction
    print("BST_1")
    binary_search_tree_1.print_tree()
    print("BST_2")
    binary_search_tree_2.print_tree()

    # Calculate minimum absolute difference
    solution = Solution()

    test_1 = solution.getMinimumDifference(bst_1)
    test_2 = solution.getMinimumDifference(bst_2)

    print(f"Test 1 Output: {test_1}")
    print(f"Test 2 Output: {test_2}")