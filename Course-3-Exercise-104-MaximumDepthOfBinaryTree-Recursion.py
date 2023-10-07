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

        # Use a queue to keep track of nodes
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

    def printTree(self):
        def helper(root):
            if root:
                print(root.val)
                helper(root.left)
                helper(root.right)

        helper(self.root)

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1


if __name__ == '__main__':

    # Inputs
    root1 = [3,9,20,None,None,15,7]
    root2 = [1,None,2]

    # Construct Trees
    binary_tree1 = BinaryTree()
    binary_tree2 = BinaryTree()

    tree1 = binary_tree1.listToBinaryTree(root1)
    tree2 = binary_tree2.listToBinaryTree(root2)

    # Test for tree construction
    binary_tree1.printTree()
    binary_tree2.printTree()

    # Leetcode problem: Test for depth
    solution = Solution()

    tree1_depth = solution.maxDepth(tree1)
    tree2_depth = solution.maxDepth(tree2)

    print(f"Tree1 Depth: {tree1_depth}")
    print(f"Tree2 Depth: {tree2_depth}")