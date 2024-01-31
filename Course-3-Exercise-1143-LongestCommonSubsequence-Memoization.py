from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            # Base case: If either string is now empty, we can't match
            # up anymore characters.
            if p1 == len(text1) or p2 == len(text2):
                return 0

            # Option 1: We don't include text1[p1] in the solution.
            option_1 = memo_solve(p1 + 1, p2)

            # Option 2: We include text1[p1] in the solution, as long as
            # a match for it in text2 at or after p2 exists.
            first_occurance = text2.find(text1[p1], p2)
            option_2 = 0
            if first_occurance != -1:
                option_2 = 1 + memo_solve(p1 + 1, first_occurance + 1)

            # Return the best option.
            return max(option_1, option_2)

        return memo_solve(0, 0)


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