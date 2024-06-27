from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            # Quick break, since we the sum of positige numbers cannot equal zero
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, result)
        return result

    def twoSum(self, nums: List[int], i: int, result: List[List[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                result.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] ==nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1



if __name__ == '__main__':
    # Inputs
    nums1 = [-1, 0, 1, 2, -1, -4]
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

