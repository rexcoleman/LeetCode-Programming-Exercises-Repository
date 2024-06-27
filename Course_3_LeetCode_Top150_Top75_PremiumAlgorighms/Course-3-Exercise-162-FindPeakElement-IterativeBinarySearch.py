from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        # This pattern accounts for the case whe len(nums) = 2
        # It is equivalent to left <= right
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        return left if nums[left] >= nums[right] else right





if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [1, 2, 3, 1]
    expected_output_1 = 2
    nums_2 = [1, 2, 1, 3, 5, 6, 4]
    expected_output_2 = 5
    nums_3 = [1, 2]
    expected_output_3 = 1
    nums_4 = [1]
    expected_output_4 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    test_1 = solution_1.findPeakElement(nums_1)
    test_2 = solution_2.findPeakElement(nums_2)
    test_3 = solution_3.findPeakElement(nums_3)
    test_4 = solution_4.findPeakElement(nums_4)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3 Result: {test_3} \nExpected Result: {expected_output_3}")
    print(f"\nTest 4 Result: {test_4} \nExpected Result: {expected_output_4}")