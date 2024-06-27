class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {0: 0,
              1: 1,
              2: 1
              }

        def dp_recurse(n: int):
            if n in dp:
                return dp[n]
            dp[n] = dp_recurse(n - 1) + dp_recurse(n - 2) + dp_recurse(n - 3)

            return dp[n]

        return dp_recurse(n)

if __name__ == '__main__':

    # Inputs and Expected Outputs
    n_1 = 4
    expected_output_1 = 4
    n_2 = 25
    expected_output_2 = 1389537
    n_3 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.tribonacci(n_1)
    test_2 = solution_2.tribonacci(n_2)

    # Prnt Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 1 Output: {test_2} \nExpected Output: {expected_output_2}")

