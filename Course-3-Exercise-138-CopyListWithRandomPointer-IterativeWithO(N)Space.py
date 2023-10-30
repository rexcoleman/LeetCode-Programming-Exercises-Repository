class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        # Creating a visited dictionary to hold old node reference as "key" and new node reference as the "value"
        self.visited = {}

    def getClonedNode(self, node):
        # If node exists then
        if node:
            # Check if its in the visited dictionary
            if node in self.visited:
                # If its in the visited dictionary then return the new node reference from the dictionary
                return self.visited[node]
            else:
                # Otherwise create a new node, save the reference in the visited dictionary and return it.
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return head
        old_node = head
        # Creating the new head node.
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        # Iterate on the linked list until all nodes are cloned.
        while old_node != None:
            # Get the clones of the nodes referenced by random and next pointers.
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            # Move one step ahead in the linked list.
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]





# Function to create linkedlist from the input nested list
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


    # Return linked list head
    return nodes[0]



def lindedListToNestedList(head):
    index_map = {}
    output = []
    i = 0
    node = head
    while node:
        index_map[node] = i
        i += 1
        node = node.next
    i = 0
    node = head
    while node:
        index = None if node.random is None else index_map[node.random]
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


    # Create an output nested list from the cloned linked list
    output_1 = lindedListToNestedList(new_head_1)
    output_2 = lindedListToNestedList(new_head_2)
    output_3 = lindedListToNestedList(new_head_3)

    # Print the output
    print(f"Output 1: {output_1}: \nExpected Output 1: [[7,None],[13,0],[11,4],[10,2],[1,0]]")
    print(f"Output 2: {output_2}: \nExpected Output 2: [[1,1],[2,1]]")
    print(f"Output 3: {output_3}: \nExpected Output 3: [[3,None],[3,0],[3,None]]")
