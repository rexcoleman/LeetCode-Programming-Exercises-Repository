from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    # Be careful of the indexing since dp grid has additional row and column
                    dp[r + 1][c + 1] = 1 + min(dp[r][c],
                                               dp[r + 1][c],
                                               dp[r][c + 1]
                                               )
                    max_side = max(max_side, dp[r + 1][c + 1])
        return max_side * max_side





if __name__ == '__main__':
    # Inputs and Expected Outputs
    matrix_1 = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    expected_output_1 = 4
    matrix_2 = [
        ["0", "1"],
        ["1", "0"]
    ]
    expected_output_2 = 1
    matrix_3 = [
        ["0"]
    ]
    expected_output_3 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.maximalSquare(matrix_1)
    test_2 = solution_2.maximalSquare(matrix_2)
    test_3 = solution_3.maximalSquare(matrix_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")