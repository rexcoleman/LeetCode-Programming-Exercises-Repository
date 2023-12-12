from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacalGrid: List[List[int]]) -> int:
        m = len(obstacalGrid)
        n = len(obstacalGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacalGrid[0][0] == 1:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacalGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1, m):
            obstacalGrid[i][0] = int(obstacalGrid[i][0] == 0 and obstacalGrid[i - 1][0] == 1)

        # Filling the values for the first row
        for j in range(1, n):
            obstacalGrid[0][j] = int(obstacalGrid[0][j] == 0 and obstacalGrid[0][j - 1] == 1)

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for i in range(1, m):
            for j in range(1, n):
                if obstacalGrid[i][j] == 0:
                    obstacalGrid[i][j] = obstacalGrid[i - 1][j] + obstacalGrid[i][j - 1]
                else:
                    obstacalGrid[i][j] = 0

        # Return value stored in rightmost bottommost cell. That is the destination.
        return obstacalGrid[m - 1][n - 1]




if __name__ == '__main__':

    # Inputs and Expected Outputs:
    obstacleGrid_1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    expected_output_1 = 2
    obstacleGrid_2 = [[0, 1], [0, 0]]
    expected_output_2 = 1

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.uniquePathsWithObstacles(obstacleGrid_1)
    test_2 = solution_2.uniquePathsWithObstacles(obstacleGrid_2)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
