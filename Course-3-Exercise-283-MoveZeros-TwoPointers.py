from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1


if __name__ == '__main__':

    # Inputs and Expected Outputs:
    nums_1 = [0, 1, 0, 3, 12]
    expected_output_1 = [1, 3, 12, 0, 0]
    nums_2 = [0]
    expected_output_2 = [0]
    nums_3 = [0,0,1]
    expected_output_3 = [1, 0, 0]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.moveZeroes(nums_1)
    test_2 = solution_2.moveZeroes(nums_2)
    test_3 = solution_3.moveZeroes(nums_3)

    # Print Results
    print(f"\nTest 1 Output: {nums_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {nums_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {nums_3} \nExpected Output: {expected_output_3}")