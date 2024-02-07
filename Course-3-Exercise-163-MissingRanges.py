from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        output = []
        if not nums:
            output.append([lower, upper])
            return output
        if nums[0] > lower:
            output.append([lower, nums[0] - 1])
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] + 1:
                output.append([nums[i - 1] + 1, nums[i] - 1])
        if nums[-1] < upper:
            output.append([nums[-1] + 1, upper])

        return output


if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [0, 1, 3, 50, 75]
    lower_1 = 0
    upper_1 = 99
    expected_output_1 = [[2, 2], [4, 49], [51, 74], [76, 99]]
    nums_2 = [-1]
    lower_2 = -1
    upper_2 = -1
    expected_output_2 = []

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.findMissingRanges(nums_1, lower_1, upper_1)
    test_2 = solution_2.findMissingRanges(nums_2, lower_2, upper_2)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")