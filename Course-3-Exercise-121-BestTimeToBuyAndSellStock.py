class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # initialize min price and max profit
        min_price = float('inf')
        max_profit = 0

        # O(N) running time complexity
        for price in prices:
            # if price < min_price: this increases profit
            min_price = min(price, min_price)
            # this is the definition of profit
            profit = price - min_price
            # if profit > max_profit: this increases profit
            max_profit = max(profit, max_profit)
        return max_profit


solution = Solution()

prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]

profit1 = solution.maxProfit(prices1)
profit2 = solution.maxProfit(prices2)

print(f'Max profit from prices1 list: {profit1}')
print(f'Max profit from prices2 list: {profit2}')