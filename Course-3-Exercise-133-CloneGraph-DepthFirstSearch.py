from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Graph:
    def __init__(self):
        self.root = None

    def build_graph(self, adjList):
        if not adjList:
            return None
        nodes = [Node(i + 1) for i in range(len(adjList))]
        for i, neighbors in enumerate(adjList):
            for n in neighbors:
                nodes[i].neighbors.append(nodes[n - 1])

        return nodes[0]

    def print_graph(self, node):
        if not node:
            return []
        visited = set()
        adjList = [[] for _ in range(len(self._dfs(node, visited)))]
        for v in visited:
            adjList[v.val - 1] = [neighbor.val for neighbor in v.neighbors]
        return adjList

    def _dfs(self, node, visited):
        if node in visited:
            return visited
        visited.add(node)
        for neighbor in node.neighbors:
            self._dfs(neighbor, visited)
        return visited


class Solution:
    def __init__(self):
        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        self.visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        # If the node was already visited before. Return the clone from the visited dictionary.
        if node in self.visited:
            return self.visited[node]

        # Create a clone for the given node. Note that we don't have cloned neighbors as of now, hence [].
        clone_node = Node(node.val, [])

        # The key is original node and value being the clone node.
        self.visited[node] = clone_node

        # Iterate through the neighbors to generate their clones
        # and prepare a list of cloned neighbors to be added to the cloned node.

        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node


if __name__ == '__main__':

    # Inputs and Outputs
    adjList_1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    expected_output_1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    adjList_2 = [[]]
    expected_output_2 = [[]]
    adjList_3 = []
    expected_output_3 = []

    # Build Graphs
    graph_1 = Graph()
    graph_2 = Graph()
    graph_3 = Graph()
    g_1 = graph_1.build_graph(adjList_1)
    g_2 = graph_2.build_graph(adjList_2)
    g_3 = graph_3.build_graph(adjList_3)

    # Print to Test Graphs
    print(f"\nGraph 1 Print Test: {graph_1.print_graph(g_1)} \nExpected Output: {adjList_1}")
    print(f"\nGraph 2 Print Test: {graph_2.print_graph(g_2)} \nExpected Output: {adjList_2}")
    print(f"\nGraph 3 Print Test: {graph_3.print_graph(g_3)} \nExpected Output: {adjList_3}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.cloneGraph(g_1)
    test_2 = solution_2.cloneGraph(g_2)
    test_3 = solution_3.cloneGraph(g_3)
    output_1 = graph_1.print_graph(test_1)
    output_2 = graph_2.print_graph(test_2)
    output_3 = graph_3.print_graph(test_3)
    print(f"\nTest 1: {output_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2: {output_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3: {output_3} \nExpected Result: {expected_output_3}")




