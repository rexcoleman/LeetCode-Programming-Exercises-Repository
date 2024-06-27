from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # It is impossible to sell stock on the first day.
        # Set -infinity as initial value for curr_hold

        curr_hold, curr_profit = -float('inf'), 0

        for stock_price in prices:
            prev_hold, prev_profit = curr_hold, curr_profit

            # Either keep hold or buy stock today at stock price
            curr_hold = max(prev_hold, prev_profit - stock_price)

            # Either keep not_hold or of sell out of stock today at stock price
            curr_profit = max(prev_profit, prev_hold + stock_price)

        # Maximum profit must be in not-hold state
        return curr_profit





if __name__ == '__main__':

    # Inputs
    prices1 = [7, 1, 5, 3, 6, 4]
    prices2 = [1, 2, 3, 4, 5]
    prices3 = [7, 6, 4, 3, 1]

    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()

    test_1 = solution_1.maxProfit(prices1)
    test_2 = solution_2.maxProfit(prices2)
    test_3 = solution_3.maxProfit(prices3)

    print(f"Maximum Profit 1: {test_1}")
    print(f"Maximum Profit 2: {test_2}")
    print(f"Maximum Profit 3: {test_3}")
