import math
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Define Variables
        fast = k
        len_nums = len(nums)
        curr_sum = max_sum = sum(nums[:k])

        # Edge Case
        if len_nums <= k:
            return sum(nums) / len_nums

        # Iterate through nums
        while fast < len_nums:
            curr_sum += nums[fast] - nums[fast - k]
            max_sum = max(max_sum, curr_sum)
            fast += 1

        return max_sum / k


if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [1, 12, -5, -6, 50, 3]
    k_1 = 4
    expected_output_1 = 12.75000
    nums_2 = [5]
    k_2 = 1
    expected_output_2 = 5.00000

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.findMaxAverage(nums_1, k_1)
    test_2 = solution_2.findMaxAverage(nums_2, k_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1:.5f} \nExpected Output: {expected_output_1:.5f}")
    print(f"\nTest 2 Output: {test_2:.5f} \nExpected Output: {expected_output_2:.5f}")