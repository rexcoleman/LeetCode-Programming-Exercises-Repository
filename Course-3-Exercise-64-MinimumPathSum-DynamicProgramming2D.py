from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) <= 0 or grid is None:
            return 0

        m, n = len(grid), len(grid[0])

        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


if __name__ == '__main__':

    # Inputs and Expected Outputs
    grid_1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    expected_output_1 = 7
    grid_2 = [[1, 2, 3], [4, 5, 6]]
    expected_output_2 = 12

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.minPathSum(grid_1)
    test_2 = solution_2.minPathSum(grid_2)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")