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
                queue.append(current.left)
            i += 1

            # Right child
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1
        return self.root

    def print_tree(self):
        def helper(root):
            if root:
                print(root.val)
                helper(root.left)
                helper(root.right)

        helper(self.root)

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        if root:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth




if __name__ == '__main__':

    # Inputs
    root1 = [3,9,20,None,None,15,7]
    root2 = [1,None,2]

    # Construct Tree
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()

    tree1 = binary_tree_1.listToBinaryTree(root1)
    tree2 = binary_tree_2.listToBinaryTree(root2)

    # Test for Tree Construction
    binary_tree_1.print_tree()
    binary_tree_2.print_tree()

    # Test for depth
    solution = Solution()

    tree1_depth = solution.maxDepth(tree1)
    tree2_depth = solution.maxDepth(tree2)

    print(f"Tree1 Depth: {tree1_depth}")
    print(f"Tree2 Depth: {tree2_depth}")


