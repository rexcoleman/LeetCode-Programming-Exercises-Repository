from functools import cache


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1_000_000_007
        SQ_MATRIX = [[1,1,2],[1,0,0],[0,1,1]]
        SIZE = 3  # Width/Length of square matrix

        def matrix_product(m1, m2):
            """Return product of 2 square matrices."""
            nonlocal MOD, SIZE
            # Result matrix `ans` will also be a square matrix with same dimensions.
            ans = [[0] * SIZE for _ in range(SIZE)]
            for row in range(SIZE):
                for col in range(SIZE):
                    curr_sum = 0
                    for k in range(SIZE):
                        curr_sum += (m1[row][k] * m2[k][col]) % MOD
                    ans[row][col] = curr_sum
            return ans

        def matrix_expo(n):
            """Perform matrix multiplication n times."""
            curr = SQ_MATRIX
            for _ in range(1, n):
                curr = matrix_product(curr, SQ_MATRIX)
            # The answer will be cur[0][0] * f(2) + cur[0][1] * f(1) + cur[0][2] * p(2)
            return (curr[0][0] * 2 + curr[0][1] * 1 + curr[0][2] * 1) % MOD

        # Handle base case scenarios
        if n <= 2:
            return n

        return matrix_expo(n - 2)


if __name__ == '__main__':

    # Inputs and Expected Outputs
    n_1 = 3
    expected_output_1 = 5
    n_2 = 1
    expected_output_2 = 1

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.numTilings(n_1)
    test_2 = solution_2.numTilings(n_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")