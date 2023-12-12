class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i: j + 1]


if __name__ == '__main__':

    # Inputs and Expected Outputs
    s_1 = "babad"
    expected_output_1 =  "bab"
    s_2 = "cbbd"
    expected_output_2 = "bb"
    s_3 = "aaaaa"
    expected_output_3 = "aaaaa"

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.longestPalindrome(s_1)
    test_2 = solution_2.longestPalindrome(s_2)
    test_3 = solution_3.longestPalindrome(s_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")