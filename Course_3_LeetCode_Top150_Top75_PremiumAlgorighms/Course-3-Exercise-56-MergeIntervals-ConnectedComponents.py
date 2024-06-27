import collections
from typing import List
from collections import defaultdict

class Solution:

    def overlap(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]

    # generate graph where there is an undirected edge between intervals u
    # and v if u and v overlap.
    def buildGraph(self, intervals):
        graph = defaultdict(list)

        for i, interval_i in enumerate(intervals):
            for j in range(i + 1, len(intervals)):
                if self.overlap(interval_i, intervals[j]):
                    graph[tuple(interval_i)].append(intervals[j])
                    graph[tuple(intervals[j])].append(interval_i)

        return graph

    # merges all of the nodes in this connected component into one interval.
    def mergeNodes(self, nodes):
        min_start = min(node[0] for node in nodes)
        max_end = max(node[1] for node in nodes)
        return [min_start, max_end]

    # gets the connected components of the interval overlap graph.
    def getComponents(self, graph, intervals):
        visited = set()
        comp_number = 0
        nodes_in_comp =  defaultdict(list)

        def markComponentDFS(start):
            stack = [start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])

        # mark all nodes in the same connected component with the same integer.
        for interval in intervals:
            if tuple(interval) not in visited:
                markComponentDFS(interval)
                comp_number += 1

        return nodes_in_comp, comp_number

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        graph = self.buildGraph(intervals)
        nodes_in_comp, number_of_comps = self.getComponents(graph, intervals)

        # all intervals in each connected component must be merged.
        return [self.mergeNodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]





if __name__ == '__main__':

    #Inputs
    intervals_1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals_2 = [[1, 4], [4, 5]]

    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.merge(intervals_1)
    test_2 = solution_2.merge(intervals_2)

    print(f"Test 1: {test_1}")
    print("Expected Output 1: [[1,6],[8,10],[15,18]]")
    print(f"Test 2: {test_2}")
    print("Expected Output 2: [[1,5]]")