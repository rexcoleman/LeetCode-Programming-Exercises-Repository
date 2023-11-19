from collections import defaultdict
from typing import List


class Solution(object):

    WHITE = 1
    GRAY = 2
    BLACK = 3


    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)

        # A pair [a, b] in the input represents edge from b --> a
        for course, prereq_course in prerequisites:
            adj_list[prereq_course].append(course)

        topological_sorted_order = []
        is_possible = True

        # By default all vertices are WHITE
        color = {k: Solution.WHITE for k in range(numCourses)}

        def dfs(node):
            nonlocal is_possible

            # Don't recurse further if we found a cycle already
            if not is_possible:
                return

            # Start the recursion
            color[node] = Solution.GRAY

            # Traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                        # An edge to a GRAY vertex represents a cycle
                        is_possible = False

            # Recursion ends. We mark it as black
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == Solution.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []




if __name__ == '__main__':
    # Inputs and Expected Outputs
    numCourses_1 = 2
    prerequisites_1 = [[1, 0]]
    expected_output_1 = [0, 1]
    numCourses_2 = 4
    prerequisites_2 = [[1,0],[2,0],[3,1],[3,2]]
    expected_output_2 = [0,2,1,3]
    numCourses_3 = 1
    prerequisites_3 = []
    expected_output_3 = [0]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    result_1 = solution_1.findOrder(numCourses_1, prerequisites_1)
    result_2 = solution_2.findOrder(numCourses_2, prerequisites_2)
    result_3 = solution_3.findOrder(numCourses_3, prerequisites_3)
    print(f"\nTest 1: {result_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2: {result_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3: {result_3} \nExpected Result: {expected_output_3}")