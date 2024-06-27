class Solution:
    def findPeakElement(self, nums):

        len_nums = len(nums)
        # Case for only one element
        if len_nums == 1:
            return 0

        # Case for either end is a peak
        if nums[1] < nums[0]:
          return 0
        if nums[-2] < nums[-1]:
            return len_nums -1

        left, right = 1, len_nums - 2

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid -1] and nums[mid] > nums[mid +1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1



if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [1, 2, 3, 1]
    expected_output_1 = 2
    nums_2 = [1, 2, 1, 3, 5, 6, 4]
    expected_output_2 = 5
    nums_3 = [1]
    expected_output_3 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.findPeakElement(nums_1)
    test_2 = solution_2.findPeakElement(nums_2)
    test_3 = solution_3.findPeakElement(nums_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
