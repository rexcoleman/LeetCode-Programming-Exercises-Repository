from collections import deque

class Node:
    def __init__(self, val: int=0, left: 'Node'=None, right: 'Node'=None, next: 'Node'=None ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class BinaryTree:
    def __init__(self):
        self.root = None

    def listToBinaryTree(self, values):
        if not values:
            return None
        # Create root node
        self.root = Node(values[0])
        # Create deque to track nodes
        queue = deque([self.root])
        i = 1
        while i < len(values):
            current = queue.popleft()
            # Left node
            if i < len(values) and values[i] is not None:
                current.left = Node(values[i])
                queue.append(current.left)
            i += 1
            # Right node
            if i < len(values) and values[i] is not None:
                current.right = Node(values[i])
                queue.append(current.right)
            i += 1
        return self.root


    def binaryTreeToValuesList(self, root):
        output = []
        if not root:
            return []
        # Use a deque to keep track of nodes
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
        while output and output[-1] is None:
            output.pop()
        return output

    def binaryTreeToNextList(self, root):
        if root is None:
            return []
        output = []
        current = root
        bottom_row_current_search = False
        next_level_start = None
        while current and bottom_row_current_search is False:
            # Starting node of the current level
            level_start = current
            if level_start.left is None and level_start.right is None:
                bottom_row_current_search = True
            while current:
                output.append(current.val)
                if bottom_row_current_search is True:
                    if current.left:
                        next_level_start = current.left
                    if current.right:
                        next_level_start = current.right
                # Check if there is a next node on the same level
                if current.next is None:
                    output.append('#')
                    bottom_row_current_search = False
                # Move to the next node on the same level

                current = current.next
            # Move to the first node on the next level
            if level_start.left is not None:
                current = level_start.left
            elif level_start.right is not None:
                current = level_start.right
            else:
                current = next_level_start
                next_level_start = None
        return output

class Solution:

    def processChild(self, childNode, prev, leftmost):
        if childNode:
            # If the "prev" pointer is already set i.e. if we already found at least
            # one node on the next level, set its next pointer
            if prev:
                prev.next = childNode
            else:
                # Else it means this child node is the first node we have encountered on the next level,
                # so, we set the leftmost pointer
                leftmost = childNode
            prev = childNode
        return prev, leftmost

    def connect(self, root: 'Node') -> Node:
        if not root:
            return root
        # The root node is the only node on the first level
        # and hence its the leftmost node for that level
        leftmost = root
        # We have no idea about the structure of the tree, so we keep going until we do find the last level.
        # The nodes on the last level won't have any children
        while leftmost:
            # "prev" tracks the latest node on the "next" level while "curr" tracks
            # the latest node on the current level.
            prev, curr = None, leftmost

            # We reset this so that we can re-assign it to the leftmost node of the next level.
            # Also, if there isn't one, this would help break us out of the outermost loop.
            leftmost = None

            # Iterate on the nodes in the current level using the next pointers already established.
            while curr:
                # Process both the children and update the prev and leftmost pointers as necessary.
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)

                # Move onto the next node.
                curr = curr.next
        return root


if __name__ == '__main__':

    # Inputs and expected outputs
    root_1 = [1, 2, 3, 4, 5, None, 7]
    output_1 = [1,'#',2,3,'#',4,5,7,'#']
    root_2 = []
    output_2 = []

    # Construct binary trees
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    bt_1 = binary_tree_1.listToBinaryTree(root_1)
    bt_2 = binary_tree_2.listToBinaryTree(root_2)

    # Print to test trees
    tree_1_test = binary_tree_1.binaryTreeToValuesList(bt_1)
    tree_2_test = binary_tree_2.binaryTreeToValuesList(bt_2)
    print(f"\nTree 1 Print Test: {tree_1_test} \nExpected Result: {root_1}")
    print(f"\nTree 2 Print Test: {tree_2_test} \nExpected Result: {root_2}")

    # Run tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.connect(bt_1)
    test_2 = solution_2.connect(bt_2)

    # Convert binary trees into output lists
    result_1 = binary_tree_1.binaryTreeToNextList(test_1)
    result_2 = binary_tree_2.binaryTreeToNextList(test_2)

    # Print test results
    print(f"\nTest 1 Result: {result_1} \nExpected Result: {output_1}")
    print(f"\nTest 2 Result: {result_2} \nExpected Result: {output_2}")
