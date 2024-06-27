from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # If text1 doesn't reference the shortest string, swap them.
        if len(text2) < len(text1):
            text1, text2 = text2, text1

        # The previous column starts with all 0's and like before is 1
        # more than the length of the first word.
        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text1) + 1)

        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
            # The current column becomes the previous one.
            previous, current = current, previous

        # The original problem's answer is in previous[0]. Return it.
        return previous[0]


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