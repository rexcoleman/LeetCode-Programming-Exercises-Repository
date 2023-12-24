from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # Define Variables
        sum_nums = sum(nums)
        left_prefix = 0

        # Edge case(s)
        if len(nums) == 1:
            return 0

        # Loop
        for pivot_index in range(len(nums)):
            if pivot_index > 0:
                left_prefix += nums[pivot_index - 1]
            if left_prefix == (sum_nums - nums[pivot_index]) / 2:
                return pivot_index
        return -1


if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [1, 7, 3, 6, 5, 6]
    expected_output_1 = 3
    nums_2 = [1, 2, 3]
    expected_output_2 = -1
    nums_3 = [2, 1, -1]
    expected_output_3 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.pivotIndex(nums_1)
    test_2 = solution_2.pivotIndex(nums_2)
    test_3 = solution_3.pivotIndex(nums_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")