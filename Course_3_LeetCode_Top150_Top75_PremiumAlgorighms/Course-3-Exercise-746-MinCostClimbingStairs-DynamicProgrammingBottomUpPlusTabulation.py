from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        minimum_cost = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            take_one_step = minimum_cost[i - 1] + cost[i - 1]
            take_two_step = minimum_cost[i - 2] + cost[i - 2]
            minimum_cost[i] = min(take_one_step, take_two_step)
        return minimum_cost[-1]


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