from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost, t2_cost = float('inf'), float('inf')
        t1_profit, t2_profit = 0, 0

        for price in prices:
            # the maximum profit if only one transaction is allowed
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)
            # reinvest the gained profit in the second transaction
            t2_cost = min(t2_cost, -t1_profit + price)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit


if __name__ == '__main__':

    # Inputs and Expected Outputs:
    prices_1 = [3, 3, 5, 0, 0, 3, 1, 4]
    expected_output_1 = 6
    prices_2 = [1, 2, 3, 4, 5]
    expected_output_2 = 4
    prices_3 = [7, 6, 4, 3, 1]
    expected_output_3 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.maxProfit(prices_1)
    test_2 = solution_2.maxProfit(prices_2)
    test_3 = solution_3.maxProfit(prices_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")