from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        # Find the index of the pivot element (the smallest element)
        # At the end, pivot = left
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        # Binary search over an inclusive range [left_boundary ~ right_boundary]
        def binarySearch(left_boundary, right_boundary, target):
            left, right = left_boundary, right_boundary
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return - 1


        # Binary search over elements on the pivot element's left
        if (answer := binarySearch(0, left - 1, target)) != -1:
            return answer

        # Binary search over elements on the pivot element's right
        return binarySearch(left, n - 1, target)




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