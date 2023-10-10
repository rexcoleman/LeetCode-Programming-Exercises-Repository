from collections import deque

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
        # Use a deque to keep track of tree nodes
        queue = deque([self.root])
        i = 1
        # Iterate through values to add nodes to tree (BFS)
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
        # Return root node
        return self.root

    def print_tree(self):
        # If there is no tree root then there is nothing to print
        if not self.root:
            return
        # Use a deque to keep track of nodes
        queue = deque([self.root])
        # Iterate through tree nodes and print values (BFS)
        while queue:
            current = queue.popleft()
            print(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


class Solution:
    def compute_depth(self, node) -> int:
        # Return tree depth in O(d) time
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx: int, d: int, node: TreeNode) -> bool:
        # Last level nodes are returned from 0 to 2**d - 1 (left to right)
        # Return True if last level idx node exists
        # Binary search with O(d) complexity
        left, right = 0, 2**d -1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None

    def countNodes(self, root: TreeNode) -> int:
        # if the tree is empty
        if not root:
            return 0
        d = self.compute_depth(root)
        # If the tree contains 1 node
        if d == 0:
            return 1
        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right)
        # Perform binary search to check how many nodes exist
        left, right = 0, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1
        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # and left nodes on the last level
        return (2**d - 1) + left




if __name__ == '__main__':

    # Inputs
    root1 = [1, 2, 3, 4, 5, 6]
    root2 = []
    root3 = [1]

    # Construct trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    binary_tree_3 = BinaryTree()

    bt_1 = binary_tree_1.list_to_binary_tree(root1)
    bt_2 = binary_tree_2.list_to_binary_tree(root2)
    bt_3 = binary_tree_3.list_to_binary_tree(root3)

    # Print to test tree construction
    print(f"Tree 1 Print Test:")
    binary_tree_1.print_tree()
    print(f"Tree 2 Print Test:")
    binary_tree_2.print_tree()
    print(f"Tree 3 Print Test:")
    binary_tree_3.print_tree()

    # Count Tree Nodes
    solution = Solution()

    test_1 = solution.countNodes(bt_1)
    test_2 = solution.countNodes(bt_2)
    test_3 = solution.countNodes(bt_3)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")
    print(f"Test 3: {test_3}")
