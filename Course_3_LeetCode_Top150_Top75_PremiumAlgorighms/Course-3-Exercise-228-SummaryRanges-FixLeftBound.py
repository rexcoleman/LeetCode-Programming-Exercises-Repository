class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        i = 0

        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1

            if start != nums[i]:
                ranges.append(str(start) + "->" + str(nums[i]))
            else:
                ranges.append(str(nums[i]))

            i += 1

        return ranges

if __name__ == "__main__":
    solution = Solution()

    nums1 = [0, 1, 2, 4, 5, 7]

    nums2 = [0, 2, 3, 4, 6, 8, 9]

    outcome1 = solution.summaryRanges(nums1)
    outcome2 = solution.summaryRanges(nums2)

    print(f"Outcome1: {outcome1}")
    print(f"Outcome2: {outcome2}")