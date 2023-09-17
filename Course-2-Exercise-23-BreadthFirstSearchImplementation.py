class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False

def breadth_first_search(start_node):

    # FIFO: first item we insert will be the first one to take out
    queue = [start_node]
    start_node.visited = True

    # we keep iterating (considering the neighbors) until the queue becomes empty
    while queue:

        # we remove and return the first item we have inserted into the list data structure
        actual_node = queue.pop(0)
        print(actual_node.name)

        # let's consider the neighbors of the actual node one by one
        for n in actual_node.adjacency_list:
            if not n.visited:
                n.visited = True
                queue.append(n)


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
    node3.adjacency_list.append(node4)

    # run the breadth first search algorithm
    breadth_first_search(node1)

