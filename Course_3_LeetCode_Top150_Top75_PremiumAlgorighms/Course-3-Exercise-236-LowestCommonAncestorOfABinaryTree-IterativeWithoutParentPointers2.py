from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None
        self.p_node = None
        self.q_node = None

    def inputNodeAssignment(self, node, p, q):
        if node.val == p:
            self.p_node = node
            print(f"Found P Node: {self.p_node.val}")
            return self.p_node
        if node.val == q:
            self.q_node = node
            print(f"Found q Node: {self.q_node.val}")
            return self.q_node

    def listToBinaryTree(self, values, p, q):
        if not values or not p or not q:
            return None
        self.root = TreeNode(values[0])
        if self.root.val == p or self.root.val == q:
            self.inputNodeAssignment(self.root, p, q)
        queue = deque([self.root])
        i = 1
        while i < len(values):
            current = queue.popleft()
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                if current.left.val == p or current.left.val == q:
                    self.inputNodeAssignment(current.left, p, q)
                queue.append(current.left)
            i += 1
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                if current.right.val == p or current.right.val == q:
                    self.inputNodeAssignment(current.right, p, q)
                queue.append(current.right)
            i += 1
        return self.root

    def binaryTreeToList(self, root):
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

    # Three static flags to keep track of post-order traversal.
    # Both left and right traversal pending for a node.
    # Indicates the nodes children are yet to be traversed.
    BOTH_PENDING = 2
    # Left traversal done.
    LEFT_DONE = 1
    # Both left and right traversal done for a node.
    # Indicates the node can be popped off the stack.
    BOTH_DONE = 0

    def lowestCommonAncestor(self, root, p: Optional[TreeNode], q: Optional[TreeNode]):

        # Initialize the stack with the root node.
        stack = [(root, Solution.BOTH_PENDING)]
        # This flag is set when either one of p or q is found.
        one_node_found = False
        # This is used to keep track of LCA index.
        LCA_index = -1

        # We do a post order traversal of the binary tree using stack
        while stack:
            parent_node, parent_state = stack[-1]
            a = parent_node.val
            # If the parent_state is not equal to BOTH_DONE,
            # this means the parent_node can't be popped of yet.
            if parent_state != Solution.BOTH_DONE:
                # If both child traversals are pending
                if parent_state == Solution.BOTH_PENDING:
                    # Check if the current parent_node is either p or q.
                    if parent_node == p or parent_node == q:
                        # If one_node_found is set already, this means we have found both the nodes.
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            # Otherwise, set one_node_found to True,
                            # to mark one of p and q is found.
                            one_node_found = True

                            # Save the current top index of stack as the LCA_index
                            LCA_index = len(stack) - 1

                    # If both pending, traverse the left child first
                    child_node = parent_node.left
                else:
                    # traverse right child
                    child_node = parent_node.right

                # Update the node state at the top of the stack
                # Since we have visited one more child.
                stack.pop()
                stack.append((parent_node, parent_state - 1))

                # Add the child node to the stack for traversal.
                if child_node:
                    stack.append((child_node, Solution.BOTH_PENDING))
            else:
                # If the parent_state of the node is both done,
                # the top node could be popped off the stack.
                # i.e. If LCA_index is equal to length of stack. Then we decrease LCA_index by 1.
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()
        return None



if __name__ == '__main__':

    # Inputs and Expected Outputs
    root_1 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p_1 = 5
    q_1 = 1
    expected_output_1 = 3
    root_2 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p_2 = 5
    q_2 = 4
    expected_output_2 = 5
    root_3 = [1, 2]
    p_3 = 1
    q_3 = 2
    expected_output_3 = 1

    # Construct Binary Trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    binary_tree_3 = BinaryTree()
    bt_1 = binary_tree_1.listToBinaryTree(root_1, p_1, q_1)
    bt_2 = binary_tree_2.listToBinaryTree(root_2, p_2, q_2)
    bt_3 = binary_tree_3.listToBinaryTree(root_3, p_3, q_3)

    # Print To Test Tree Construction
    print(f"\nBinary Tree 1 Print Test: {binary_tree_1.binaryTreeToList(bt_1)} \nExpected Output: {root_1}")
    print(f"\nBinary Tree 2 Print Test: {binary_tree_2.binaryTreeToList(bt_2)} \nExpected Output: {root_2}")
    print(f"\nBinary Tree 3 Print Test: {binary_tree_3.binaryTreeToList(bt_3)} \nExpected Output: {root_3}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.lowestCommonAncestor(bt_1, binary_tree_1.p_node, binary_tree_1.q_node)
    test_2 = solution_2.lowestCommonAncestor(bt_2, binary_tree_2.p_node, binary_tree_2.q_node)
    test_3 = solution_3.lowestCommonAncestor(bt_3, binary_tree_3.p_node, binary_tree_3.q_node)


    # Print Results
    print(f"\nTest 1 Output: {test_1.val} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2.val} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3.val} \nExpected Output: {expected_output_3}")