import math
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # solve special cases
        if not prices or k == 0:
            return 0

        if k * 2 > n:
            res = 0
            for i, j in zip(prices[1:], prices[:-1]):
                res += max(0, i - j)
            return res

        # dp[i][used_k][ishold] = balance
        # i = index in prices which represents the stock trading day
        # ishold: 0 nothold, 1 hold
        a = [-math.inf] * 2
        b = [[-math.inf] * 2 for _ in range(k + 1)]
        dp = [[[-math.inf] * 2 for _ in range(k + 1)] for _ in range(n)]

        # set starting value
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]


        # fill the array
        for i in range(1, n):
            for j in range(k + 1):
                # transition equation
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                # you can't hold stock without any transaction
                if j > 0:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        res = max(dp[n-1][j][0] for j in range(k + 1))
        return res




if __name__ == '__main__':

    # Inputs and Expected Outputs:
    k_1 = 2
    prices_1 = [2,4,1]
    expected_output_1 = 2
    k_2 = 2
    prices_2 = [3,2,6,5,0,3]
    expected_output_2 = 7

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.maxProfit(k_1, prices_1)
    test_2 = solution_2.maxProfit(k_2, prices_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")