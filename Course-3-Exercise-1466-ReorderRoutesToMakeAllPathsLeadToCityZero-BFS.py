from collections import deque
from typing import List


class Solution:

    def dfs(self, adj_list, visited, from_node):
        change = 0
        visited[from_node] = True
        for to_node in adj_list[from_node]:
            if not visited[abs(to_node)]:
                change += self.dfs(adj_list, visited, abs(to_node)) + (1 if to_node > 0 else 0)
        return change


    def minReorder(self, n: int, connections: [List[List[int]]]) -> int:

        adj_list = [[] for _ in range(n)]
        for c in connections:
            adj_list[c[0]].append(c[1])
            adj_list[c[1]].append(-c[0])

        visited = [False] * len(adj_list)
        change = 0
        queue = deque([0])
        while queue:
            from_node = queue.popleft()
            visited[from_node] = True
            for to_node in adj_list[from_node]:
                if not visited[abs(to_node)]:
                    if to_node > 0:
                        change += 1
                    queue.append(abs(to_node))
        return change


if __name__ == '__main__':

    # Inputs and Expected Outputs
    n_1 = 6
    connections_1 = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    expected_output_1 = 3
    n_2 = 5
    connections_2 = [[1, 0], [1, 2], [3, 2], [3, 4]]
    expected_output_2 = 2
    n_3 = 3
    connections_3 = [[1, 0], [2, 0]]
    expected_output_3 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.minReorder(n_1,connections_1)
    test_2 = solution_2.minReorder(n_2, connections_2)
    test_3 = solution_3.minReorder(n_3, connections_3)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")