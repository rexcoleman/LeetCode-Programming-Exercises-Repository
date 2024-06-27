from functools import lru_cache
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            min_cost = float('inf')
            for coin in coins:
                res = dfs(rem - coin)
                if res != -1:
                    min_cost = min(min_cost, res + 1)
            return min_cost if min_cost != float('inf') else -1


        return dfs(amount)


if __name__ == '__main__':

    # Inputs and Expected Outputs
    coins_1 = [1, 2, 5]
    amount_1 = 11
    expected_output_1 = 3
    coins_2 = [2]
    amount_2 = 3
    expected_output_2 = -1
    coins_3 = [1]
    amount_3 = 0
    expected_output_3 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.coinChange(coins_1, amount_1)
    test_2 = solution_2.coinChange(coins_2, amount_2)
    test_3 = solution_3.coinChange(coins_3, amount_3)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3 Result: {test_3} \nExpected Result: {expected_output_3}")
