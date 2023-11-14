from typing import Optional
from collections import deque


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
        # Construct nodes
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

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        visited = {}

        # Put the first node in the queue
        queue = deque([node])
        # Clone the node and put it in the visited dictionary.
        visited[node] = Node(node.val, [])

        # Start BFS traversal
        while queue:
            # Pop a node say "current" from the from the front of the queue.
            current = queue.popleft()
            # Iterate through all the neighbors of the node
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and put in the visited, if not present already
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the newly encountered node to the queue.
                    queue.append(neighbor)
                # Add the clone of the neighbor to the neighbors of the clone node "current".
                visited[current].neighbors.append(visited[neighbor])
        # Return the clone of the node from visited.
        return visited[node]




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
    print_test_1 = graph_1.print_graph(g_1)
    print_test_2 = graph_2.print_graph(g_2)
    print_test_3 = graph_3.print_graph(g_3)
    print(f"\nPrint Test Grapht 1: {print_test_1} \nExpected Result: {adjList_1}")
    print(f"\nPrint Test Grapht 2: {print_test_2} \nExpected Result: {adjList_2}")
    print(f"\nPrint Test Grapht 3: {print_test_3} \nExpected Result: {adjList_3}")

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.cloneGraph(g_1)
    test_2 = solution_2.cloneGraph(g_2)
    test_3 = solution_3.cloneGraph(g_3)

    # Print Results
    output_1 = graph_1.print_graph(test_1)
    output_2 = graph_2.print_graph(test_2)
    output_3 = graph_3.print_graph(test_3)
    print(f"\nTest 1: {output_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2: {output_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3: {output_3} \nExpected Result: {expected_output_3}")


