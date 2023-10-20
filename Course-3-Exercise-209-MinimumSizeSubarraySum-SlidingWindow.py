from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = left = right = 0
        result = len(nums) + 1
        while right < len(nums):
            total += nums[right]
            while total >= target:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        return result if result <= len(nums) else 0







if __name__ == '__main__':

    # Inputs
    target1 = 7
    nums1 = [2, 3, 1, 2, 4, 3]
    target2 = 4
    nums2 = [1, 4, 4]
    target3 = 11
    nums3 = [1, 1, 1, 1, 1, 1, 1, 1]

    # Run tests

    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()

    test_1 = solution_1.minSubArrayLen(target1, nums1)
    test_2 = solution_2.minSubArrayLen(target2, nums2)
    test_3 = solution_3.minSubArrayLen(target3, nums3)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")
    print(f"Test 3: {test_3}")