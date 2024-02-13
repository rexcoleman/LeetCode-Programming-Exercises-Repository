from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = 0
        nums.sort()
        i = 1
        while i < len(nums) - 1:
            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp
            i += 2


if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [3, 5, 2, 1, 6, 4]
    expected_output_1 = '[3, 5, 1, 6, 2, 4] or [1,6,2,5,3,4]'
    nums_2 = [6, 6, 5, 6, 3, 8]
    expected_output_2 = [6, 6, 5, 6, 3, 8]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.wiggleSort(nums_1)
    test_2 = solution_2.wiggleSort(nums_2)
    print(f"\nTest 1 Output: {nums_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {nums_2} \nExpected Output: {expected_output_2}")