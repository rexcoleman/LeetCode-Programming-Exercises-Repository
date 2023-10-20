from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total_sum = sum(nums)
        if total_sum < target:
            return 0
        length = len(nums)
        for i in range(length):
            nums[i], total_sum = total_sum, total_sum - nums[i]
        result = length
        nums.append(0)
        for left_pointer in range(length - 1, -1, -1):
            if nums(left_pointer) >= target:
                min_length = min(length, left_pointer + result - 1)
                while nums[left_pointer] - nums[result] >= target:
                    result = min_length - left_pointer
                    min_length -= 1
        return result




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