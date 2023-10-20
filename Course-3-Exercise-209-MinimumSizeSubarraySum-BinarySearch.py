from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total_sum = sum(nums)
        if total_sum < target:
            return 0
        length = len(nums)
        for i in range(length):
            nums[i], total_sum = total_sum, total_sum - nums[i]
        min_length = length
        # Append zero to the end of the list to enable the min_length calculations
        # End inialized at this index
        nums.append(0)
        # Iterate in reverse because the list is sorted with
        # decreasing cumulative values.
        # If this element is > target then every we know that from the original list
        # The element at this index plus all the elements to the right are > target
        for i in range(length - 1, -1, -1):
            # We are looking to reduce the length to find the min.
            # This is why we use (i + min_length - 1).  This places the distance between
            # i and end to be one index shorter than min_length
            end = min(length, i + min_length - 1)
            # This loop applies when we have a sub-array with a sum >= target
            # It first conditionally reduces the min_length
            # It then uses binary search (mid) to determine where to place end (end = mid)
            # The result is that we have the shortest array with a sum >= target
            # starting at index i
            while nums[i] - nums[end] >= target:
                # Condition to reduce min_length
                if min_length > end - i:
                    min_length = end - i
                mid = (i + end) // 2
                while nums[i] - nums[mid] < target and mid < end - 1:
                    mid = (mid + end) // 2
                if mid == end:
                    break
                end = mid
        return min_length



if __name__ == '__main__':

    # Inputs
    target1 = 7
    nums1 = [2, 3, 1, 2, 4, 1, 1, 1, 3]
    target2 = 4
    nums2 = [1, 4, 4]
    target3 = 11
    nums3 = [1, 1, 1, 1, 1, 1, 1, 1]

    # Run tests

    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()

    test_1 = solution_1.minSubArrayLen(target1, nums1)
    test_2 = solution_2.minSubArrayLen(target2, nums2)
    test_3 = solution_3.minSubArrayLen(target3, nums3)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")
    print(f"Test 3: {test_3}")