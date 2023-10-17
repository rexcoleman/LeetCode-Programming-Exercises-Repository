from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Take curr variable to keep the current maximum jump...
        curr = nums[0]
        # Traverse all the elements through loop...
        for i in range(1, len(nums)):
            # If the current index 'i' is less than current maximum jump 'curr'...
            # It means there is no way to jump to current index...
            # so we should return false...
            if curr == 0:
                return False
            curr -= 1
            # Update the current maximum jump...
            curr = max(curr, nums[i])
        # It’s possible to reach the end of the array...
        return True

if __name__ == '__main__':

    # Inputs
    nums1 = [2, 3, 1, 1, 4]
    nums2 = [3, 2, 1, 0, 4]

    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.canJump(nums1)
    test_2 = solution_2.canJump(nums2)

    print(f"Maximum Profit 1: {test_1}")
    print(f"Maximum Profit 2: {test_2}")