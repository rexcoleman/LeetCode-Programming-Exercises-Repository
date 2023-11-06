from collections import deque


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
        queue = deque([self.root])
        i = 1
        while i < len(values[0]):
            current = queue.popleft()
            if i < len(values[0]) and values[0][i] is not None:
                current.left = TreeNode(values[0][i])
                queue.append(current.left)
            i += 1
            if i <len(values[0]) and values[0][i] is not None:
                current.right = TreeNode(values[0][i])
                queue.append(current.right)
            i += 1
        return self.root

    def binarySearchTreeToList(self, root):
        if not root:
            return []
        output = []
        queue = deque([self.root])
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


class BSTIterator:

    def __init__(self, root: TreeNode):
        # Stack for the recursion simulation
        self.stack = []
        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        # For a given node, add all the elements in the leftmost branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left

    def next (self) -> int:
        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()
        # Need to maintain the invariant. If the node has a right child, call the
        # helper function for the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


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

    # Run Tests


    def testCommands(commands):
        bst_iterator = BSTIterator(bst)
        for i in range(1, len(commands)):
            if command[i] == 'next':
                test = bst_iterator.next()
                print(f"Output: {test}, Expected Output: {expected_output[i]}")
            else:
                test = bst_iterator.hasNext()
                print(f"Output: {test}, Expected Output: {expected_output[i]}")

    testCommands(command)

