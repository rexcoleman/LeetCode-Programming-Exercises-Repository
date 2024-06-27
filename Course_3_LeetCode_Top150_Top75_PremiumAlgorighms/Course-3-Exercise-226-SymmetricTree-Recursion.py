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

        # Use a deque to keep track of the nodes
        queue = deque([self.root])
        i = 1

        # Iterate through values to keep to add nodes to the tree
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
        # Special case
        if not root:
            return None
        # Return the function recursively
        return self.is_same(root.left, root.right)

    # A tree is symmetric if the left subtree is a mirror reflection of the right subtree
    def is_same(self, left, right):
        # If both root nodes are None pointers: return True
        if left is None and right is None:
            return True
        # If either root node is None but not both: return False
        if left is None or right is None:
            return False
        # If node values differ: return False
        if left.val != right.val:
            return False
        # Return True if: i) values are the same and ii) subtrees are symmetric
        return self.is_same(left.left, right.right) and \
            self.is_same(left.right, right.left)


if __name__ == '__main__':
    # Inputs
    root1 = [1, 2, 2, 3, 4, 4, 3]
    root2 = [1, 2, 2, None, 3, None, 3]

    # Construct trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()

    bt_1 = binary_tree_1.list_to_binary_tree(root1)
    bt_2 = binary_tree_2.list_to_binary_tree(root2)

    # Test tree construction with print function
    print("Tree 1 Print Test")
    binary_tree_1.print_tree()
    print("Tree 2 Print Test")
    binary_tree_2.print_tree()

    # Test if tree is symmetric
    solution = Solution()

    test_tree_1 = solution.is_symmetric(bt_1)
    test_tree_2 = solution.is_symmetric(bt_2)

    print(f"Outcome 1: {test_tree_1}")
    print(f"Outcome 2: {test_tree_2}")
