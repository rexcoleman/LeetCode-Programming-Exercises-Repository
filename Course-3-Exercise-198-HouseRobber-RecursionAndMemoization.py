from typing import List


class Solution:

    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.robFrom(0, nums)
    def robFrom(self, i, nums):
        # No more houses left to examine.
        if i >= len(nums):
            return 0

        # Return cached value.
        if i in self.memo:
            return self.memo[i]

        # Recursive relation evaluation to get the optimal answer.
        ans = max(self.robFrom(i+ 1, nums), self.robFrom(i + 2, nums) + nums[i])

        # Cache for future use.
        self.memo[i] = ans
        return ans

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
