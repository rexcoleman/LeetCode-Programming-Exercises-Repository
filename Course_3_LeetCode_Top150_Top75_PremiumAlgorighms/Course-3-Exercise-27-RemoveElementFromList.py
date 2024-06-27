class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # set index pointer to start of nums
        index = 0

        # iterate through nums
        for a in range(len(nums)):
            # a skips over items with value (val) which index writes over them
            if nums[a] != val:
                nums[index] = nums[a]
                index += 1
        print(nums[:index])
        print(index)
        return index



solution = Solution()

nums = [0,1,2,2,3,0,4,2]
val = 2

print(solution.removeElement(nums, val))
