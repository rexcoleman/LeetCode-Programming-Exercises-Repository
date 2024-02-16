from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        zero_count = 0
        zero_set = set()
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] == 0:
                zero_count += 1
                zero_set.add(right)
                if len(zero_set) > 1:
                    del_idx = min(zero_set)
                    left = del_idx + 1
                    zero_set.remove(del_idx)
            max_ones = max(max_ones, right - left + 1)
            right += 1

        return max_ones


if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [1, 0, 1, 1, 0]
    expected_output_1 = 4
    nums_2 = [1, 0, 1, 1, 0, 1]
    expected_output_2 = 4

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.findMaxConsecutiveOnes(nums_1)
    test_2 = solution_2.findMaxConsecutiveOnes(nums_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
