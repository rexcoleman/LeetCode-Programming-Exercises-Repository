class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # start with the last (greatest) values in each list
        i = m - 1
        j = n - 1
        # pointer that starts at the end of nums1
        k = len(nums1) - 1

        # we want to merge nums2 into nums 1.  when nums 2 is empty
        # then the loop ends
        while j >= 0:
            # only apply this condition when we have values remaining to compare in nums1
            # if the item in nums1 is greater then move to the end and decrement i by 1
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            # if the item in nums2 is greater then move to the end of nums 1 and decrement by 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            # decrement k by 1 to complete the loop iteration
            k -= 1


solution = Solution()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

solution.merge(nums1, m, nums2, n)
print(nums1)