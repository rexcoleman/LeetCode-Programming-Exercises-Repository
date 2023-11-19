from collections import deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            # An adjacency list for this directed graph uses the index as the prerequisite course
            # and the value as the course that relies on the prerequisite course
            adj[prerequisite[1]].append(prerequisite[0])
            # The indegree states how many remaining prerequisites are required (value)
            # before taking the course (index)
            indegree[prerequisite[0]] += 1

        queue = deque()
        # Start with nodes that have zero indegrees
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        nodesVisited = 0
        while queue:
            node = queue.popleft()
            nodesVisited += 1

            # We use this for loop to reduce indegrees and look for nodes
            # with zero indegrees to add to queue
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return nodesVisited == numCourses

if __name__ == '__main__':
    # Inputs and Expected Outputs
    numCourses_1 = 2
    prerequisites_1 = [[1, 0]]
    expected_output_1 = True
    numCourses_2 = 2
    prerequisites_2 = [[1, 0], [0, 1]]
    expected_output_2 = False

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    result_1 = solution_1.canFinish(numCourses_1, prerequisites_1)
    result_2 = solution_2.canFinish(numCourses_2, prerequisites_2)
    print(f"\nTest 1: {result_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2: {result_2} \nExpected Result: {expected_output_2}")

