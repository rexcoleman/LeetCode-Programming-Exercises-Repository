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
        self.root = TreeNode(values[0][0])
        # Use deque to construct tree using breadth first search traversal
        queue = deque([self.root])
        i = 1
        while i < len(values[0]):
            current = queue.popleft()
            # Left node
            if i < len(values[0]) and values[0][i] is not None:
                current.left = TreeNode(values[0][i])
                queue.append(current.left)
            i += 1
            # Right node
            if i < len(values[0]) and values[0][i] is not None:
                current.right = TreeNode(values[0][i])
                queue.append(current.right)
            i += 1
        return self.root

    def binarySearchTreeToList(self, root):
        if not root:
            return []
        output = []
        # Use deque to track nodes uses breadth first search traversal
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if current is not None:
                output.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                output.append(None)
        # Remove trailing None values
        while output and output[-1] is None:
            output.pop()
        return output

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        # Array containing all the nodes in the sorted order
        self.nodes_sorted = []
        print(self.nodes_sorted)
        # Pointer to the next smallest element in the BST
        self.index = -1
        # Call to flatten the input binary search tree
        self._inorder(root)

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.nodes_sorted)


if __name__ == '__main__':

    # Inputs and Expected Outputs
    command = ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    command_value = [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []]
    expected_output = [None, 3, 7, True, 9, True, 15, True, 20, False]

    # Construct Binary Search Tree
    binary_search_tree = BinarySearchTree()
    bst = binary_search_tree.listToBinarySearchTree(command_value[0])

    # Print to Test Binary Search Tree
    print_test = binary_search_tree.binarySearchTreeToList(bst)
    print(f"\nBST Print Test: {print_test} \nExpected Result: {command_value[0]}")

    # Run Test
    bst_iterator = BSTIterator(bst)

    def testCommands(commands):
        for i in range(1, len(commands)):
            if commands[i] == 'next':
                test = bst_iterator.next()
                print(f"Output: {test}, Expected Output: {expected_output[i]}")
            else:
                test = bst_iterator.hasNext()
                print(f"Output: {test}, Expected Output: {expected_output[i]}")

    testCommands(command)

