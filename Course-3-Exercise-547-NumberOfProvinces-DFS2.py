from collections import defaultdict
from typing import List


class Solution:
    def findCircleNum(self, isConnected: [List[List[int]]]) -> int:
        graph = defaultdict(list)

        if not isConnected:
            return 0

        n = len(isConnected)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        visit = [False] * n

        def dfs(u):
            for v in graph[u]:
                if visit[v] == False:
                    visit[v] = True
                    dfs(v)

        count = 0
        for i in range(n):
            if visit[i] == False:
                count += 1
                visit[i] = True
                dfs(i)

        return count

if __name__ == '__main__':

    # Inputs and Expected Outputs
    isConnected_1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    expected_output_1 = 2
    isConnected_2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    expected_output_2 = 3
    isConnected_3 = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    expected_output_3 = 1

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.findCircleNum(isConnected_1)
    test_2 = solution_2.findCircleNum(isConnected_2)
    test_3 = solution_3.findCircleNum(isConnected_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
