from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        len_nums = len(nums)
        left = ans = 0
        k = 1

        # Skip leading zeros
        for right in range(len_nums):
            if k >= 0 and nums[right] == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            curr = right - left + 1 if k == 1 else right - left
            ans = max(ans, curr)
        return ans if ans < len_nums else ans - 1


if __name__ == '__main__':

    # Inputs and Expected Outputs:
    nums_1 = [1, 1, 0, 1]
    expected_output_1 = 3
    nums_2 = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    expected_output_2 = 5
    nums_3 = [1, 1, 1]
    expected_output_3 = 2
    nums_4 = [0, 0, 0]
    expected_output_4 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    test_1 = solution_1.longestSubarray(nums_1)
    test_2 = solution_2.longestSubarray(nums_2)
    test_3 = solution_3.longestSubarray(nums_3)
    test_4 = solution_4.longestSubarray(nums_4)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
    print(f"\nTest 4 Output: {test_4} \nExpected Output: {expected_output_4}")