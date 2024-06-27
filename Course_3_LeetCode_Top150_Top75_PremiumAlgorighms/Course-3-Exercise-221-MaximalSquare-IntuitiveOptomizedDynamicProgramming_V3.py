from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0

        m, n = len(matrix), len(matrix[0])
        result = 0
        dp = [[0] * n for _ in range(2)] # 2-rowed dp array
        for i in range(m):
            for j in range(n):
                # i%2 (or i&1) alternates between dp[0] and dp[1]
                dp[i % 2][j] = 0 if matrix[i][j] == '0' else \
                    1 + min(dp[i % 2][j - 1] if j > 0 else 0,
                        dp[1 - i % 2][j - 1] if j > 0 else 0,
                        dp[1 - i % 2][j]
                    )
                result = dp[i%2][j] if dp[i%2][j] > result else result
        return result * result


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