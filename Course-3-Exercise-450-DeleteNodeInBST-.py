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

    def listToBinarySearchTree(self, values):
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        i = 1
        while i < len(values):
            current = queue.popleft()
            if values[i] and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            if values[i] and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1
        return self.root

    def binarySearchTreeToList(self, root):
        output = []
        if not root:
            return output
        queue = deque([root])
        while queue:
            current = queue.popleft()
            if current is not None:
                output.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                output.append(None)
        while output and output[-1] is None:
            output.pop()
        return output


class Solution:
    class Solution:
        def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
            pass


if __name__ == '__main__':

    # Inputs and Expected Outputs
    root_1 = [5, 3, 6, 2, 4, None, 7]
    key_1 = 3
    expected_output_1 = [5, 4, 6, 2, None, None, 7]
    root_2 = [5, 3, 6, 2, 4, None, 7]
    key_2 = 0
    expected_output_2 = [5, 3, 6, 2, 4, None, 7]
    root_3 = []
    key_3 = 0
    expected_output_3 = []

    # Construct BinarySearchTrees
    binary_search_tree_1 = BinarySearchTree()
    binary_search_tree_2 = BinarySearchTree()
    binary_search_tree_3 = BinarySearchTree()
    bst_1 = binary_search_tree_1.listToBinarySearchTree(root_1)
    bst_2 = binary_search_tree_2.listToBinarySearchTree(root_2)
    bst_3 = binary_search_tree_3.listToBinarySearchTree(root_3)

    # Print to Test BST
    print(f"\nBST 1 Print Test: {binary_search_tree_1.binarySearchTreeToList(bst_1)} \nExpected Output: {'Drake is cool'}")
    print(f"\nBST 2 Print Test: {binary_search_tree_2.binarySearchTreeToList(bst_2)}")
    print(f"\nBST 3 Print Test: {binary_search_tree_3.binarySearchTreeToList(bst_3)}")
