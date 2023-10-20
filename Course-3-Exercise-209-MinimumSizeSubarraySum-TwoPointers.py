from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        if not length:
            return 0
        total_sum = 0
        left_pointer = 0
        right_pointer = 0
        result = length + 1
        while total_sum < target:
            total_sum += nums[right_pointer]
            right_pointer += 1
            while total_sum >= target:
                if right_pointer - left_pointer < result:
                    result = right_pointer - left_pointer
                total_sum -= nums[left_pointer]
                left_pointer += 1
            if right_pointer == length:
                break
        if result > length:
            return 0
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