
class Node:

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjacency_list = []


def depth_first_search(start_node):

    # LIFO: last item we insert is the first item we take out
    stack = [start_node]

    # iterate until the stack becomes empty
    while stack:
        # the pop() function returns with the last item we have inserted - O(1)
        actual_node = stack.pop()
        print(actual_node.name)

        for n in actual_node.adjacency_list:
            # if the node has not been visited so far
            if not n.visited:
                n.visited = True
                # insert the item into the stack
                stack.append(n)

if __name__ == '__main__':


    # we can create the nodes or vertices
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node5 = Node('E')

    # we have to handle the neighbors
    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    depth_first_search(node1)