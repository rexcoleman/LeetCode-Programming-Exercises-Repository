from typing import List


class Solution:

    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        # Special handling for empty case.
        if not nums:
            return 0

        N = len(nums)
        rob_next_plus_one = 0
        rob_next = nums[N - 1]

        # DP table calculations
        for i in range(N - 2, -1, -1):
            # Same as recursive solution.
            current = max(nums[i] + rob_next_plus_one, rob_next)

            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current

        return rob_next


if __name__ == '__main__':
    # Inputs and Expected Outputs
    nums_1 = [1,2,3,1]
    expected_output_1 = 4
    nums_2 = [2,7,9,3,1]
    expected_output_2 = 12


    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.rob(nums_1)
    test_2 = solution_2.rob(nums_2)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
