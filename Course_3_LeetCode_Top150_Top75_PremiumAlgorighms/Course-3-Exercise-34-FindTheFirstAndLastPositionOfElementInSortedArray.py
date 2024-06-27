from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower_bound = self.findBound(nums, target, True)
        if (lower_bound == -1):
            return [-1, -1]
        upper_bound = self.findBound(nums, target, False)

        return [lower_bound, upper_bound]


    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        N = len(nums)
        begin, end = 0, N - 1
        while begin <= end:
            mid = int((begin + end) // 2)
            if nums[mid] == target:
                if isFirst:
                    # This means we found our lower bound.
                    if mid == begin or nums[mid - 1] < target:
                        return mid
                    # Search on the left side for the bound.
                    end = mid - 1
                else:
                    # This means we found our upper bound.
                    if mid == end or nums[mid + 1] > target:
                        return mid

                    # Search on the right side for the bound.
                    begin = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        return -1






if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [5, 7, 7, 8, 8, 10]
    target_1 = 8
    expected_output_1 = [3, 4]
    nums_2 = [5, 7, 7, 8, 8, 10]
    target_2 = 6
    expected_output_2 = [-1, -1]
    nums_3 = []
    target_3 = 0
    expected_output_3 = [-1, -1]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.searchRange(nums_1, target_1)
    test_2 = solution_2.searchRange(nums_2, target_2)
    test_3 = solution_3.searchRange(nums_3, target_3)

    # Print Results
    print(f"\nTest 1 Results: {test_1} \nExpected Results: {expected_output_1}")
    print(f"\nTest 2 Results: {test_2} \nExpected Results: {expected_output_2}")
    print(f"\nTest 3 Results: {test_3} \nExpected Results: {expected_output_3}")
