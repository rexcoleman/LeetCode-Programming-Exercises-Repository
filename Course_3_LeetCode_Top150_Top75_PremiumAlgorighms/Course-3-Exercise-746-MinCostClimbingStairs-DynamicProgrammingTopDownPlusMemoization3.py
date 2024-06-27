from functools import cache
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @cache

        def minimum_cost(i):
            if i <= 1:
                return 0

            down_one = cost[i - 1] + minimum_cost(i - 1)
            down_two = cost[i - 2] + minimum_cost(i - 2)
            return min(down_one, down_two)

        return minimum_cost(len(cost))




if __name__ == '__main__':

    # Inputs and Expected Outputs
    cost_1 = [10, 15, 20]
    expected_output_1 = 15
    cost_2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    expected_output_2 = 6

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.minCostClimbingStairs(cost_1)
    test_2 = solution_2.minCostClimbingStairs(cost_2)

    # Prnt Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 1 Output: {test_2} \nExpected Output: {expected_output_2}")