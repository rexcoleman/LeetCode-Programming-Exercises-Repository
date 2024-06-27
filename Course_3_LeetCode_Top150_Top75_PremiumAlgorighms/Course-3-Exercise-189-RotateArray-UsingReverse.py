from typing import List


class Solution:

    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)




if __name__ == '__main__':

    # Inputs
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    nums2 = [-1, -100, 3, 99]
    k2 = 2

    test_1 = Solution()
    test_2 = Solution()

    t_1 = test_1.rotate(nums1, k1)
    t_2 = test_2.rotate(nums2, k2)

    print(f"Test 1: {nums1}")
    print(f"Test 2: {nums2}")
