from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2

            # Case 1: find target
            if nums[mid] == target:
                return mid

            # Case 2: subarray on mid's left is sorted
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Case 3: subarray on mid's right is sorted.
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1




if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [4, 5, 6, 7, 0, 1, 2]
    target_1 = 0
    expected_output_1 = 4
    nums_2 = [4, 5, 6, 7, 0, 1, 2]
    target_2 = 3
    expected_output_2 = -1
    nums_3 = [1]
    target_3 = 0
    expected_output_3 = -1

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.search(nums_1, target_1)
    test_2 = solution_2.search(nums_2, target_2)
    test_3 = solution_3.search(nums_3, target_3)

    # Print Results
    print(f"\nTest 1 Results: {test_1} \nExpected Results: {expected_output_1}")
    print(f"\nTest 2 Results: {test_2} \nExpected Results: {expected_output_2}")
    print(f"\nTest 3 Results: {test_3} \nExpected Results: {expected_output_3}")