from typing import List


class Solution:
    def dfs(self, node, adj, visit, inStack):
        # If the node is already in the stack, we have a cycle.
        if inStack[node]:
            return True
        if visit[node]:
            return False
        # Mark the current node as visited and part of current recursion stack.
        visit[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, visit, inStack):
                return True
        # Remove the node from the stack.
        inStack[node] = False
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        # An adjacency list for this directed graph uses the index as the prerequisite course
        # and the value as the course that requires the prerequisite course
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])

        visit = [False] * numCourses
        inStack = [False] * numCourses
        for i in range(numCourses):
            if self.dfs(i, adj, visit, inStack):
                return False
        return True


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