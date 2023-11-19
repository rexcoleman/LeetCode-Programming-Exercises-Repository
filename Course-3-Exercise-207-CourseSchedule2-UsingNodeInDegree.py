from collections import defaultdict, deque
from typing import List


class Solution(object):
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Prepare the graph
        adj_list = defaultdict(list)
        indegree = {}
        for course, prerequisite_course in prerequisites:
            adj_list[prerequisite_course].append(course)

            # Record each node's in-degree
            indegree[course] = indegree.get(course, 0) + 1

        # Queue for maintainig list of nodes that have 0 in-degree
        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])

        topological_sorted_order = []

        # Until there are no nodes in the Q
        while zero_indegree_queue:
            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)

            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []




if __name__ == '__main__':

    # Inputs and Expected Outputs
    numCourses_1 = 2
    prerequisites_1 = [[1, 0]]
    expected_output_1 = [0, 1]
    numCourses_2 = 4
    prerequisites_2 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    expected_output_2 = [0, 2, 1, 3]
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