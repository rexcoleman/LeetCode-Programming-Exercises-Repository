from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect_left(sub, num)
            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num
        return len(sub)


if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [10, 9, 2, 5, 3, 7, 101, 18]
    expected_output_1 = 4
    nums_2 = [0, 1, 0, 3, 2, 3, 2]
    expected_output_2 = 4
    nums_3 = [7, 7, 7, 7, 7, 7, 7]
    expected_output_3 = 1

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.lengthOfLIS(nums_1)
    test_2 = solution_2.lengthOfLIS(nums_2)
    test_3 = solution_3.lengthOfLIS(nums_3)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3 Result: {test_3} \nExpected Result: {expected_output_3}")