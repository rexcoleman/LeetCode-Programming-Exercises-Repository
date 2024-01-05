from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = ans = flips = 0
        len_nums = len(nums)
        flips_index = set()

        if len_nums < k:
            return len_nums - 1


        for right in range(len_nums):
            if nums[right] == 0:
                flips_index.add(right)
                flips += 1
            while flips > k:
                flips -= (left in flips_index)
                left += 1
            curr = right - left + 1
            ans = max(ans, curr)
        return ans


if __name__ == '__main__':

    # Inputs and Expected Outputs:
    nums_1 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k_1 = 2
    expected_output_1 = 6
    nums_2 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k_2 = 3
    expected_output_2 = 10

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.longestOnes(nums_1, k_1)
    test_2 = solution_2.longestOnes(nums_2, k_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")