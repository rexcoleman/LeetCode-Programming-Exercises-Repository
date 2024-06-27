from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        total_steps = len(cost)
        step_2 = min(cost[0], cost[1])

        dp = {
            0: 0,
            1: 0,
            2: step_2
        }

        def steps_recurse(steps):
            if steps - 1 in dp and steps - 2 in dp:
                dp[steps] = min(dp[steps-1] + cost[steps-1], dp[steps-2] + cost[steps-2])
                return dp[steps]
            dp[steps - 1] = steps_recurse(steps - 1)
            return min(dp[steps - 1] + cost[steps - 1], dp[steps - 2] + cost[steps - 2] )

        return steps_recurse(total_steps)




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