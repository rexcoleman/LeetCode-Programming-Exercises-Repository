class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:

    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return head

        # Creating a new weaved list of original and copied nodes.
        original_node = head
        while original_node:
            # Cloned node
            new_node = Node(original_node.val, None, None)
            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = original_node.next
            original_node.next = new_node
            original_node = new_node.next

        original_node = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original node's random pointers,
        # to assign references to random pointers for cloned nodes.
        while original_node:
            original_node.next.random = original_node.random.next if original_node.random else None
            original_node = original_node.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        pointer_original_list = head  # A->B->C
        pointer_new_list = head.next  # A'->B'->C'
        head_new = head.next
        while pointer_original_list:
            pointer_original_list.next = pointer_original_list.next.next
            pointer_new_list.next = pointer_new_list.next.next if pointer_new_list.next else None
            pointer_original_list = pointer_original_list.next
            pointer_new_list = pointer_new_list.next

        return head_new


# Function to create linkedlist from the input nested list
def createLinkedList(nested_list):
    if not nested_list:
        return None

    # Create nodes
    nodes = {}
    for i, (val, random) in enumerate(nested_list):
        nodes[i] = Node(val, None, None)
    # Random pointers
    for i, (val, random) in enumerate(nested_list):
        if random is not None:
            nodes[i].random = nodes[random]
    # Next pointers
    for i in range(len(nested_list) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]

# Create nested list output
def linkedListToNestedList(head):
    index_map = {}
    output = []
    i = 0
    node = head
    # Map nodes to indexes
    while node:
        index_map[node] = i
        i += 1
        node = node.next

    # Create nested list
    i = 0
    node = head
    while node:
        index = None if node.random == None else index_map[node.random]
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

    # Create cloned lists
    new_head_1 = solution_1.copyRandomList(head_1)
    new_head_2 = solution_2.copyRandomList(head_2)
    new_head_3 = solution_3.copyRandomList(head_3)

    # Create an output nested list from the cloned linked list
    output_1 = linkedListToNestedList(new_head_1)
    output_2 = linkedListToNestedList(new_head_2)
    output_3 = linkedListToNestedList(new_head_3)

    # Print test results
    print(f"Output 1: {output_1}: \nExpected Output 1: [[7,None],[13,0],[11,4],[10,2],[1,0]]")
    print(f"Output 2: {output_2}: \nExpected Output 2: [[1,1],[2,1]]")
    print(f"Output 3: {output_3}: \nExpected Output 3: [[3,None],[3,0],[3,None]]")