from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left






if __name__ == '__main__':

    # Inputs
    nums1 = [1,3,5,6]
    target1 = 5
    nums2 = [1, 3, 5, 6]
    target2 = 2
    nums3 = [1, 3, 5, 6]
    target3 = 7

    # Output
    test_1 = Solution()
    test_2 = Solution()
    test_3 = Solution()

    t_1 = test_1.searchInsert(nums1, target1)
    t_2 = test_2.searchInsert(nums1, target2)
    t_3 = test_3.searchInsert(nums1, target3)

    print(f"Output 1: {t_1}")
    print(f"Output 2: {t_2}")
    print(f"Output 3: {t_3}")