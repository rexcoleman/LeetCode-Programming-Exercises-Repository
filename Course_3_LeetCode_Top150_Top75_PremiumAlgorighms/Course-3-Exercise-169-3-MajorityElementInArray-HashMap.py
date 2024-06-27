class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(N) time complexity.  O(N) space complexity.
        # initialize dictionary
        num_counts = {}
        # by definition a majority item contains more than 1/2 the items in a list
        majority_count = len(nums) // 2
        for num in nums:
            # get the value and adds one each time we find a repeat value
            num_counts[num] = num_counts.get(num, 0) + 1
            # return the majority item
            if num_counts[num] > majority_count:
                return num





solution = Solution()

nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]

print(f'Nums1 = {solution.majorityElement(nums1)}')
print(f'Nums2 = {solution.majorityElement(nums2)}')