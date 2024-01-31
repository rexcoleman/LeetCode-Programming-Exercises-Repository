from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # Make a grid of 0's with len(text2) + 1 columns
        # and len(text1) + 1 rows.
        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                # If the corresponding characters for this cell are the same...
                if text2[col] == text1[row]:
                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
                # Otherwise they must be different...
                else:
                    dp_grid[row][col] = max(dp_grid[row+ 1][col], dp_grid[row][col + 1])

        # The original problem's answer is in dp_grid[0][0]. Return it.
        return dp_grid[0][0]


if __name__ == '__main__':

    # Inputs and Expected Outputs
    text1_1 = "abcde"
    text2_1 = "ace"
    expected_output_1 = 3
    text1_2 = "abc"
    text2_2 = "abc"
    expected_output_2 = 3
    text1_3 = "abc"
    text2_3 = "def"
    expected_output_3 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.longestCommonSubsequence(text1_1, text2_1)
    test_2 = solution_2.longestCommonSubsequence(text1_2, text2_2)
    test_3 = solution_3.longestCommonSubsequence(text1_3, text2_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")