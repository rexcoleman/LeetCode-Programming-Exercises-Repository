import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]

        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        return max_subarray

if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected_output_1 = 6
    nums_2 = [1]
    expected_output_2 = 1
    nums_3 = [5, 4, -1, 7, 8]
    expected_output_3 = 23

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.maxSubArray(nums_1)
    test_2 = solution_2.maxSubArray(nums_2)
    test_3 = solution_3.maxSubArray(nums_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")