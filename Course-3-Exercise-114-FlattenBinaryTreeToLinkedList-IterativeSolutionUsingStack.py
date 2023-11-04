import collections
from typing import Optional
from collections import deque
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
        # Create tree root with first list element
        self.root = TreeNode(values[0])
        # Use deque to keep track of nodes.  This is a preorder tree: root -> left -> right
        # howerver the input list in constructed in a way that requires a breadth first construction
        # left -> root -> right
        queue = deque([self.root])
        i = 1
        while i < len(values):
            current = queue.popleft()
            # Left node
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            # Right node
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1
        return self.root



    def binaryTreeToList(self, root):
        if not root:
            return []
        output = []
        # Use deque to track nodes in a breadth first manner to print: root -> left -> right
        queue = deque([root])
        while queue:
            current = queue.popleft()
            if current:
                output.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                output.append(None)
        # Remove trailing None values
        while output and output[-1] == None:
            output.pop()
        return output


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # Handle the null scenario
        if not root:
            return None

        START, END = 1, 2

        tailNode = None
        stack = deque([(root, START)])

        while stack:
            currentNode, recursionState = stack.pop()
            # We reached a leaf node. Record this as a tail
            # node and move on.
            if not currentNode.left and not currentNode.right:
                tailNode = currentNode
                continue

            # If the node is in the START state, it means we still
            # haven't processed it's left child yet.
            if recursionState == START:
                # If the current node has a left child, we add it to the stack
                # AFTER adding the current node again to the stack with the END recursion state.
                if currentNode.left:
                    stack.append((currentNode, END))
                    stack.append((currentNode.left, START))
                elif currentNode.right:
                    # In case the current node didn't have a left child
                    # we will add it's right child
                    stack.append((currentNode.right, START))
            else:
                # If the current node is in the END recursion state, that means we did process
                # one of it's children. Left if it existed, else right.
                rightNode = currentNode.right
                # If there was a left child, there must have been a leaf
                # node and so, we would have set the tailNode
                if tailNode:
                    # Establish the proper connections.
                    tailNode.right = currentNode.right
                    currentNode.right = currentNode.left
                    currentNode.left = None
                    rightNode = tailNode.right

                if rightNode:
                    stack.append((rightNode, START))



if __name__ == '__main__':

    # Inputs and Expected Outputs
    root_1 = [1, 2, 5, 3, 4, None, 6]
    expected_output_1 = [1, None, 2, None, 3, None, 4, None, 5, None, 6]
    root_2 = []
    expected_output_2 = []
    root_3 = [0]
    expected_output_3 = [0]

    # Construct binary trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    binary_tree_3 = BinaryTree()
    bt_1 = binary_tree_1.listToBinaryTree(root_1)
    bt_2 = binary_tree_2.listToBinaryTree(root_2)
    bt_3 = binary_tree_3.listToBinaryTree(root_3)

    # Print to test binary trees
    print_output_1 = binary_tree_1.binaryTreeToList(bt_1)
    print_output_2 = binary_tree_1.binaryTreeToList(bt_2)
    print_output_3 = binary_tree_1.binaryTreeToList(bt_3)
    print(f"\nPrint Test 1: {print_output_1} \nExpected Result: {root_1}")
    print(f"\nPrint Test 2: {print_output_2} \nExpected Result: {root_2}")
    print(f"\nPrint Test 3: {print_output_3} \nExpected Result: {root_3}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.flatten(bt_1)
    test_2 = solution_2.flatten(bt_2)
    test_3 = solution_3.flatten(bt_3)


    # Print Results
    result_1 = binary_tree_1.binaryTreeToList(bt_1)
    result_2 = binary_tree_2.binaryTreeToList(bt_2)
    result_3 = binary_tree_3.binaryTreeToList(bt_3)

    print(f"\nFlattened Tree 1: {result_1}\nExpected Result: {expected_output_1}")
    print(f"\nFlattened Tree 2: {result_2}\nExpected Result: {expected_output_2}")
    print(f"\nFlattened Tree 3: {result_3}\nExpected Result: {expected_output_3}")
