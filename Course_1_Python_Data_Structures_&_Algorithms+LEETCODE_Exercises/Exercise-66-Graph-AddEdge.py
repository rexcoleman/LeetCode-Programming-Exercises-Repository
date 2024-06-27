class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        v_list = []
        for vertex in self.adj_list:
            v_list.append(vertex)
        v_list.sort()
        for v in v_list:
            print(v, ':', self.adj_list[v])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False




my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)

my_graph.add_edge(1,2)

my_graph.print_graph()



"""
    EXPECTED OUTPUT:
    ----------------
    1 : [2]
    2 : [1]

"""