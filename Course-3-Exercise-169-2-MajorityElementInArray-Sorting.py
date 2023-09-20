class Solution(object):

    # by definition a majority has more than hald the items in a list
    # by sorting and finding the item at the midpoint we will find the majority
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]


solution = Solution()

nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]

print(f'Nums1 = {solution.majorityElement(nums1)}')
print(f'Nums2 = {solution.majorityElement(nums2)}')