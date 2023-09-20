class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # by definition a majority has more than half the items in a list.
        # we are looking for the item that has more than half the items in the list
        # O(N^2) time complexity due to two nested for loops
        majority_count = len(nums)//2

        for num in nums:
            count = 0
            for elem in nums:
                if elem == num:
                    count += 1
                    if count > majority_count:
                        return num



solution = Solution()

nums1 = [3,2,3]
nums2 = [2,2,1,1,1,2,2]

print(f'Nums1 = {solution.majorityElement(nums1)}')
print(f'Nums2 = {solution.majorityElement(nums2)}')