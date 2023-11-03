from collections import deque


class Node:
    def __init__(self, val: int=0, left: 'Node'=None, right: 'Node'=None, next: 'Node'=None):
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
        # Create the root node with the first element of values
        self.root = Node(values[0])
        # Use a deque to keep track of the nodes
        constructor_queue = deque([self.root])
        i = 1
        # Iterate list to add nodes to tree
        while i < len(values):
            current = constructor_queue.popleft()
            # Left node
            if i < len(values) and values[i] is not None:
                current.left = Node(values[i])
                constructor_queue.append(current.left)
            i += 1
            # Right node
            if i < len(values) and values[i] is not None:
                current.right = Node(values[i])
                constructor_queue.append(current.right)
            i += 1
        return self.root

    def binaryTreeToList(self, root):
        output = []
        if not root:
            return []
        # Use a deque to keep track of the nodes
        queue = deque([root])
        while queue:
            current = queue.popleft()
            if current:
                output.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                output.append(None)
        # Remove trailing none values
        while output and output[-1] is None:
            output.pop()
        return output

    def binaryTreeToNextList(self, root):
        if not root:
            return []

        output = []
        current = root

        while current:
            level_start = current  # Starting node of the current level
            while current:
                output.append(current.val)

                # Check if there is a next node on the same level
                if current.next is None:
                    output.append('#')

                current = current.next  # Move to the next node on the same level

            # Move to the first node of the next level
            current = level_start.left if level_start.left else level_start.right

        return output


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        # Initialize a queue data structure which contains
        # just the root of the tree
        queue = deque([root])

        # Outer while loop which iterates over each level
        while queue:
            # Note the size of the queue
            size = len(queue)
            # Iterate over all the nodes on the current level
            for i in range(size):
                # Pop a node from the front of the queue
                node = queue.popleft()

                # This check is important. We don't want to establish any wrong connections.
                # The queue will contain nodes from 2 levels at most at any point in time.
                # This check ensures we don't establish next pointers beyond the end of a level
                if i < size - 1:
                    node.next = queue[0]

                # Add the children, if any, to the back of the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        # Since the tree has now been modified, return the root node
        return root




if __name__ == '__main__':

    # Inputs and expected outputs
    root_1 = [1, 2, 3, 4, 5, None, 7]
    output_1 = [1,'#',2,3,'#',4,5,7,'#']
    root_2 = []
    output_2 = []

    # Create tree instances and construct binary trees from input lists
    binary_tree_1 = BinaryTree()
    binary_tree_2 = BinaryTree()
    bst_1 = binary_tree_1.listToBinaryTree(root_1)
    bst_2 = binary_tree_2.listToBinaryTree(root_2)

    # Print to test tree construction
    tree_1 = binary_tree_1.binaryTreeToList(bst_1)
    tree_2 = binary_tree_2.binaryTreeToList(bst_2)
    print(f"\nTree 1 Print Test: {tree_1} \nExpected Result: {root_1}")
    print(f"\nTree 2 Print Test: {tree_2} \nExpected Result: {root_2}")

    # Create solution instances for each test and run tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.connect(bst_1)
    test_2 = solution_2.connect(bst_2)

    # Convert binary trees to output lists
    result_1 = binary_tree_1.binaryTreeToNextList(test_1)
    result_2 = binary_tree_1.binaryTreeToNextList(test_2)

    # Print results
    print(f"\nResult 1: {result_1} \nExpected Result: {output_1}")
    print(f"\nResult 2: {result_2} \nExpected Result: {output_2}")