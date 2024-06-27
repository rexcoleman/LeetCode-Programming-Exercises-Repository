
class Node:

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjacency_list = []


def depth_first_search(node):

    node.visited = True
    print(node.name)

    for n in node.adjacency_list:
        if not n.visited:
            depth_first_search(n)



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