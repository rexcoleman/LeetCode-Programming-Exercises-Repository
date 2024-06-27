from functools import cache


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1_000_000_007

        # Handle base case scenarios
        if n <= 2:
            return n

        # f[k]: number of ways to "fully cover a board" of width k
        f = [0] * (n + 1)

        # p[k]: number of ways to "partially cover a board" of width k
        p = [0] * (n + 1)

        # initialize f and p with results for the base case scenarios
        f[1] = 1
        f[2] = 2
        p[2] = 1

        for k in range(3, n + 1):
            f[k] = (f[k-1] + f[k-2] + 2*p[k-1]) % MOD
            p[k] = (p[k-1] + f[k-2]) % MOD
        return f[n]


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