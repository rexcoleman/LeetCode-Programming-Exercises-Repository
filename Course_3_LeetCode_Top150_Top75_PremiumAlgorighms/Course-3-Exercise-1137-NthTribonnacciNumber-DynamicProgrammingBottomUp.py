class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {0: 0,
              1: 1,
              2: 1
              }
        if n < 3:
            return dp[n]
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            if i == n:
                return dp[i]


if __name__ == '__main__':

    # Inputs and Expected Outputs
    n_1 = 4
    expected_output_1 = 4
    n_2 = 25
    expected_output_2 = 1389537

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.tribonacci(n_1)
    test_2 = solution_2.tribonacci(n_2)

    # Prnt Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 1 Output: {test_2} \nExpected Output: {expected_output_2}")

