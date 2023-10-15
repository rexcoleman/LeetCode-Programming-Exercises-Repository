

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

if __name__ == '__main__':

    # Inputs
    n1 = 2
    n2 = 3

    # Run tests
    test_1 = Solution()
    test_2 = Solution()

    t_1 = test_1.climbStairs(n1)
    t_2 = test_2.climbStairs(n2)

    print(f"Test 1: {t_1}")
    print(f"Test 2: {t_2}")
