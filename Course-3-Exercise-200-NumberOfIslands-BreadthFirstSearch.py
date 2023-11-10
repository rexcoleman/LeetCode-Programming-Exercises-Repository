from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    queue = deque([(i, j)])
                    grid[i][j] = '2'
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                            xx, yy = x+dx, y + dy
                            if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == '1':
                                queue.append((xx, yy))
                                grid[xx][yy] = '2'
                    answer += 1
        return answer











if __name__ == '__main__':

    # Inputs and Expected Outputs
    grid_1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    expected_output_1 = 1

    grid_2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    expected_output_2 = 3

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.numIslands(grid_1)
    test_2 = solution_2.numIslands(grid_2)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
