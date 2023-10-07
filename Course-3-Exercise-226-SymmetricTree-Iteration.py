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
        # Create the root node from the first value
        self.root = TreeNode(values[0])
        # Use deque to keep track of nodes
        queue = deque([self.root])
        i = 1
        # Iterate through values to add nodes to tree
        while i < len(values):
            current = queue.popleft()
            # Left child
            if i < len(values) and values[i]:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1

            # Right child
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
        # Breadth first search iteration
        while queue:
            current = queue.popleft()
            print(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


class Solution:
    def is_symmetric(self, root):
        stack = [root.left, root.right]
        while stack:
            node1, node2 = stack.pop(), stack.pop()
            if node1 is None and node2 is None:
                continue
            elif (node1 is None or node2 is None) or node1.val != node2.val:
                return False
            stack.append(node1.left)
            stack.append(node2.right)
            stack.append(node1.right)
            stack.append(node2.left)
        return True


if __name__ == '__main__':
    # Inputs
    root1 = [1, 2, 2, 3, 4, 4, 3]
    root2 = [1, 2, 2, None, 3, None, 3]

    # Construct trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()

    bt_1 = binary_tree_1.list_to_binary_tree(root1)
    bt_2 = binary_tree_2.list_to_binary_tree(root2)

    # Print to test tree construction
    print("Tree 1 Print Test")
    binary_tree_1.print_tree()
    print("Tree 1 Print Test")
    binary_tree_2.print_tree()

    # Test for symmetry
    solution = Solution()

    symmetry_test_1 = solution.is_symmetric(bt_1)
    symmetry_test_2 = solution.is_symmetric(bt_2)

    print(f"Outcome 1: {symmetry_test_1}")
    print(f"Outcome 2: {symmetry_test_2}")
