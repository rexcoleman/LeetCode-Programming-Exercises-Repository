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

        # Iterate through list to add nodes to tree
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

class Solution(object):
    def invert_tree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        queue = deque([root])
        while queue:
            current = queue.popleft()
            current.left, current.right = current.right, current.left
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return root

    def tree_to_list(self, root):
        if not root:
            return []
        output = []
        queue = deque([root])
        while queue:
            current = queue.popleft()
            output.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return output


if __name__ == '__main__':

    # Inputs
    root_1 = [4, 2, 7, 1, 3, 6, 9]
    root_2 = [2, 1, 3]
    root_3 = []

    # Construct tree
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    binary_tree_3 = BinaryTree()

    tree_1 = binary_tree_1.list_to_binary_tree(root_1)
    tree_2 = binary_tree_2.list_to_binary_tree(root_2)
    tree_3 = binary_tree_3.list_to_binary_tree(root_3)


    # Test for tree construction
    print("Binary Tree 1:")
    binary_tree_1.print_tree()
    print("Binary Tree 2:")
    binary_tree_2.print_tree()
    print("Binary Tree 3:")
    binary_tree_3.print_tree()

    # Test if trees are the same
    solution = Solution()

    inverted_tree_1 = solution.invert_tree(tree_1)
    inverted_tree_2 = solution.invert_tree(tree_2)
    inverted_tree_3 = solution.invert_tree(tree_3)

    output_1 = solution.tree_to_list(inverted_tree_1)
    output_2 = solution.tree_to_list(inverted_tree_2)
    output_3 = solution.tree_to_list(inverted_tree_3)

    print(f"Outcome 1: {output_1}")
    print(f"Outcome 2: {output_2}")
    print(f"Outcome 3: {output_3}")




