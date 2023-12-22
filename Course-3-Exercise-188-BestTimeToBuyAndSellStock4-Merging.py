import math
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # solve special cases
        if not prices or k == 0:
            return 0

        # find all consecutively increasing subsequence
        transactions = []
        start = 0
        end = 0
        for i in range(1, n):
            if prices[i] >= prices[i - 1]:
                end = i
            else:
                if end > start:
                    transactions.append([start, end])
                start = i
        if end > start:
            transactions.append([start, end])

        while len(transactions) > k:
            # check delete loss
            delete_index = 0
            min_delete_loss = math.inf
            for i in range(len(transactions)):
                t = transactions[i]
                profit_loss = prices[t[1]] - prices[t[0]]
                if profit_loss < min_delete_loss:
                    min_delete_loss = profit_loss
                    delete_index = i

            # check merge loss
            merge_index = 0
            min_merge_loss = math.inf
            for i in range(1, len(transactions)):
                t1 = transactions[i-1]
                t2 = transactions[i]
                profit_loss = prices[t1[1]] - prices[t2[0]]
                if profit_loss < min_merge_loss:
                    min_merge_loss = profit_loss
                    merge_index = i

            # delete or merge
            if min_delete_loss <= min_merge_loss:
                transactions.pop(delete_index)
            else:
                transactions[merge_index - 1][1] = transactions[merge_index][1]
                transactions.pop(merge_index)

        return sum(prices[j] - prices[i] for i, j in transactions)


if __name__ == '__main__':

    # Inputs and Expected Outputs:
    k_1 = 2
    prices_1 = [2,4,1]
    expected_output_1 = 2
    k_2 = 2
    prices_2 = [3,2,6,5,0,3,1,4]
    expected_output_2 = 8

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.maxProfit(k_1, prices_1)
    test_2 = solution_2.maxProfit(k_2, prices_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")