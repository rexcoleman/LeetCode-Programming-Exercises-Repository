from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak



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