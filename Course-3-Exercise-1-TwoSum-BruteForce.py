class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]



if __name__ == "__main__":

    solution = Solution()

    nums1 = [2,7,11,15]
    target1 = 9

    nums2 = [3,2,4]
    target2 = 6

    nums3 = [3,3]
    target3 = 6

    outcome1 = solution.twoSum(nums1, target1)
    outcome2 = solution.twoSum(nums2, target2)
    outcome3 = solution.twoSum(nums3, target3)

    print(f"Outcome1: {outcome1}")
    print(f"Outcome2: {outcome2}")
    print(f"Outcome3: {outcome3}")