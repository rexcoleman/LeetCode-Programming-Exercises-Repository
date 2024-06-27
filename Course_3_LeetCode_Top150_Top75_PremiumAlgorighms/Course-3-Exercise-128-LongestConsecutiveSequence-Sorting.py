from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

        return max(longest_streak, current_streak)


if __name__ == '__main__':

    # Inputs
    nums_1 = [100, 4, 200, 1, 3, 2]
    nums_2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

    # Run tests
    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.longestConsecutive(nums_1)
    test_2 = solution_2.longestConsecutive(nums_2)

    print(f"Test 1: {test_1}")
    print("Expected Output 1: 4")
    print(f"Test 2: {test_2}")
    print("Expected Output 2: 9")