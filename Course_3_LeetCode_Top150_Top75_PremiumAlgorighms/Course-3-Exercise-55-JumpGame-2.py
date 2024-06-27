from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachableIndex = 0
        for curr in range(len(nums)):
            if curr + nums[curr] >= reachableIndex:
                reachableIndex = curr + nums[curr]
            if curr == reachableIndex:
                break
        return reachableIndex >= len(nums) - 1

if __name__ == '__main__':

    # Inputs
    nums1 = [2, 3, 1, 1, 4]
    nums2 = [3, 2, 1, 0, 4]

    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.canJump(nums1)
    test_2 = solution_2.canJump(nums2)

    print(f"Maximum Profit 1: {test_1}")
    print(f"Maximum Profit 2: {test_2}")