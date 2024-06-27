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
        # Create root with first element of values
        self.root = TreeNode(values[0])
        # Use a deque to keep track of nodes
        queue = deque([self.root])
        i = 1
        # Iterate through values to add nodes to the binary tree (BFS)
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
        # Return root at end
        return self.root

    def print_tree(self):
        if not self.root:
            return
        # Use deque to keep track of nodes
        queue = deque([self.root])
        # Iterate through nodes (BFS)
        while queue:
            current = queue.popleft()
            print(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


class Solution:
    def countNodes(self, root) -> int:
        return 1 + self.countNodes(root.right) + self.countNodes(root.left) if root else 0


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