class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
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

        # Use a queue to keep track of the nodes
        queue = [self.root]
        i = 1

        while i < len(values):
            current = queue.pop(0)
            # Left child
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
            i += 1
            # Right child
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
            i +=1
        return self.root

    def print_tree(self):
        def helper(root):
            if root:
                print(root.val)
                helper(root.left)
                helper(root.right)
        helper(self.root)

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Check if both p and q are None
        if not p and not q:
            return True
        # Check if one of p or q is None
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)

if __name__ == '__main__':

    # Inputs
    p1 = [1, 2, 3]
    q1 = [1, 2, 3]
    p2 = [1, 2]
    q2 = [1, None, 2]
    p3 = [1, 2, 1]
    q3 = [1, 1, 2]

    # Construct Tree
    binary_tree_p1 = BinaryTree()
    binary_tree_q1 = BinaryTree()
    binary_tree_p2 = BinaryTree()
    binary_tree_q2 = BinaryTree()
    binary_tree_p3 = BinaryTree()
    binary_tree_q3 = BinaryTree()

    tree_p1 = binary_tree_p1.list_to_binary_tree(p1)
    tree_q1 = binary_tree_q1.list_to_binary_tree(q1)
    tree_p2 = binary_tree_p2.list_to_binary_tree(p2)
    tree_q2 = binary_tree_q2.list_to_binary_tree(q2)
    tree_p3 = binary_tree_p3.list_to_binary_tree(p3)
    tree_q3 = binary_tree_q3.list_to_binary_tree(q3)

    # Test tree construction
    print("Binary Tree P1")
    binary_tree_p1.print_tree()
    print("Binary Tree Q1")
    binary_tree_q1.print_tree()
    print("Binary Tree P2")
    binary_tree_p2.print_tree()
    print("Binary Tree Q2")
    binary_tree_q2.print_tree()
    print("Binary Tree P3")
    binary_tree_p3.print_tree()
    print("Binary Tree Q3")
    binary_tree_q3.print_tree()

    # Test if trees are the same
    solution = Solution()

    test_1 = solution.isSameTree(tree_p1, tree_q1)
    test_2 = solution.isSameTree(tree_p2, tree_q2)
    test_3 = solution.isSameTree(tree_p3, tree_q3)

    print(f"Outcome 1: {test_1}")
    print(f"Outcome 2: {test_2}")
    print(f"Outcome 3: {test_3}")

