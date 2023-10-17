from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        price_gain = []
        for idx in range(len(prices) - 1):
            if prices[idx] < prices[idx + 1]:
                price_gain.append(prices[idx+1] - prices[idx])
        return sum(price_gain)







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
