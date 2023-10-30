class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    def copyRandomList(self, head):
        if head is None:
            return None

        # If we have already processed the current node, then we simply return the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]

        # Create a new node with the value same as the old node.
        node = Node(head.val, None, None)

        # Save this value in the hash map. This is needed since there might be
        # loops during traversal due to randomness of random pointers, and this would help us avoid them.
        self.visitedHash[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally, we update the next and random pointers for the new node created.
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

# Function to create a linked list from the given nested list
def createLinkedList(nested_list):
    if not nested_list:
        return None

    nodes = {}
    for i, (val, _) in enumerate(nested_list):
        nodes[i] = Node(val)

    for i, (_, random_node) in enumerate(nested_list):
        if random_node is not None:
            nodes[i].random = nodes[random_node]

    for i in range(len(nested_list) - 1):
        nodes[i].next = nodes[i + 1]

    return nodes[0]  # Return the head of the linked list

def lindedListToNestedList(head):
    index_map_1 = {}
    output = []
    i = 0
    node = head
    while node:
        index_map_1[node] = i
        i += 1
        node = node.next
    i = 0
    node = head
    while node:
        index = None if node.random is None else index_map_1[node.random]
        output.append([node.val, index])
        i += 1
        node = node.next

    return output









# Test code
if __name__ == '__main__':
    # Inputs
    input_list_1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    input_list_2 = [[1, 1], [2, 1]]
    input_list_3 = [[3, None], [3, 0], [3, None]]

    # Create linked list from input list
    head_1 = createLinkedList(input_list_1)
    head_2 = createLinkedList(input_list_2)
    head_3 = createLinkedList(input_list_3)

    # Create solution objects for each test
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()

    # Call the copyRandomList method with the head of the input linked list
    new_head_1 = solution_1.copyRandomList(head_1)
    new_head_2 = solution_2.copyRandomList(head_2)
    new_head_3 = solution_3.copyRandomList(head_3)


    # Create a list to output a nested list from the cloned linked list
    output_1 = lindedListToNestedList(new_head_1)
    output_2 = lindedListToNestedList(new_head_2)
    output_3 = lindedListToNestedList(new_head_3)

    # Print the output
    print(f"Output 1: {output_1}: \nExpected Output 1: [[7,None],[13,0],[11,4],[10,2],[1,0]]")
    print(f"Output 2: {output_2}: \nExpected Output 2: [[1,1],[2,1]]")
    print(f"Output 3: {output_3}: \nExpected Output 3: [[3,None],[3,0],[3,None]]")
