from collections import deque

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.p_node = None
        self.q_node = None

    def inputNodesAssignement(self, node, p, q):
        if node.val == p:
            self.p_node = node
            print(f"Found P Node: {self.p_node.val}")
            return self.p_node
        if node.val == q:
            self.q_node = node
            print(f"Found Q Node: {self.q_node.val}")
            return self.q_node

    def listToBinaryTree(self, values, p, q):
        if not values or not p or not q:
            return None
        self.root = TreeNode(values[0])
        # p and q nodes assignement
        if self.root.val == p or self.root.val == q:
            self.inputNodesAssignement(self.root, p, q)
        # Use deque to track nodes and iterate using breadth first search traversal
        queue = deque([self.root])
        i = 1
        while i < len(values):
            current = queue.popleft()
            # Left node
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                # p and q nodes assignement
                if current.left.val == p or current.left.val == q:
                    self.inputNodesAssignement(current.left, p, q)
                queue.append(current.left)
            i += 1
            # Right node
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                # p and q nodes assignement
                if current.right.val == p or current.right.val == q:
                    self.inputNodesAssignement(current.right, p, q)
                queue.append(current.right)
            i += 1
        return self.root

    def binaryTreeToList(self):
        if not self.root:
            return []
        output = []
        # Use deque to track nodes and iterate using breadth first search traversal
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

        def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

            # Initialize the stack with the root node.
            stack = [(root, Solution.BOTH_PENDING)]
            # This flag is set when either one of p or q is found.
            one_node_found = False
            # This is used to keep track of LCA index.
            LCA_Index = -1

            # We do a post order traversal of the binary tree using stack
            while stack:
                parent_node, parent_state = stack[-1]
                # If the parent_state is not equal to BOTH_DONE,
                # this means the parent_node can't be popped of yet.
                if parent_state != Solution.BOTH_DONE:
                    # If both child traversals are pending
                    if parent_state == Solution.BOTH_PENDING:
                        # Check if the current parent_node is either p or q.
                        if parent_node == p or parent_node == q:
                            # If one_node_found is set already, this means we have found both the nodes.
                            if one_node_found:
                                return stack[LCA_Index][0]
                            else:
                                # Otherwise, set one_node_found to True,
                                # to mark one of p and q is found.
                                one_node_found = True
                                # Save the current top index of stack as the LCA_index.
                                LCA_Index = len(stack) - 1
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
                    if one_node_found and LCA_Index == len(stack) - 1:
                        LCA_Index -= 1
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

    # Construct trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    binary_tree_3 = BinaryTree()
    print("\nTest 1 P and Q Nodes: Expected Values: P = 5, Q = 1")
    bt_1 = binary_tree_1.listToBinaryTree(root_1, p_1, q_1)
    print("\nTest 2 P and Q Nodes: Expected Values: P = 5, Q = 4")
    bt_2 = binary_tree_2.listToBinaryTree(root_2, p_2, q_2)
    print("\nTest 3 P and Q Nodes: Expected Values: P = 1, Q = 2")
    bt_3 = binary_tree_3.listToBinaryTree(root_3, p_3, q_3)

    # Print to test trees
    print_test_1 = binary_tree_1.binaryTreeToList()
    print_test_2 = binary_tree_2.binaryTreeToList()
    print_test_3 = binary_tree_3.binaryTreeToList()
    print(f"\nPrint Tree 1 Test: {print_test_1} \nExpected Result: {root_1}")
    print(f"\nPrint Tree 2 Test: {print_test_2} \nExpected Result: {root_2}")
    print(f"\nPrint Tree 3 Test: {print_test_3} \nExpected Result: {root_3}")


    # Run tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    lca_1 = solution_1.lowestCommonAncestor(bt_1, binary_tree_1.p_node, binary_tree_1.q_node)
    lca_2 = solution_2.lowestCommonAncestor(bt_2, binary_tree_2.p_node, binary_tree_2.q_node)
    lca_3 = solution_3.lowestCommonAncestor(bt_3, binary_tree_3.p_node, binary_tree_3.q_node)


    # Print results
    print(f"\nTest 1 Result: {lca_1.val} \nExpected Result {expected_output_1}")
    print(f"\nTest 2 Result: {lca_2.val} \nExpected Result {expected_output_2}")
    print(f"\nTest 3 Result: {lca_3.val} \nExpected Result {expected_output_3}")

