from typing import List

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1



if __name__ == '__main__':

    # Inputs
    nums1 = [-1,0,1,2,-1,-4]
    nums2 = [0, 1, 1]
    nums3 = [0, 0, 0]

    solution1 = Solution()
    solution2 = Solution()
    solution3 = Solution()

    test_1 = solution1.threeSum(nums1)
    test_2 = solution1.threeSum(nums2)
    test_3 = solution1.threeSum(nums3)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")
    print(f"Test 3: {test_3}")

    