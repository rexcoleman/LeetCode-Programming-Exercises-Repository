class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # set write pointer to index 1
        write_pointer = 1
        # iterate read pointer starting at index 1 to compare with index 0
        # when not duplicate
        # write pointer writes value and increments up
        for read_pointer in range(1, len(nums)):
            if nums[read_pointer] != nums[read_pointer - 1]:
                nums[write_pointer] = nums[read_pointer]
                write_pointer += 1
        return write_pointer

solution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1, 2]
print(solution.removeDuplicates(nums))