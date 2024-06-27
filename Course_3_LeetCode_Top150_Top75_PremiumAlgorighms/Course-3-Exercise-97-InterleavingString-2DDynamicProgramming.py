class Solution:
    def interLeave(self, s1: str, s2: str, s3: str) -> bool:
        # Intuitively this is a 2 X 2 matrix.
        # The (0, 0) cell represents the base case where s1 and s2 are empty strings.
        # This is why we have (m +1) and (n + 1).
        # We then need to reverse these +1 terms with -1 terms when comparing to the strings.
        # The dp factors (dp[i - 1][0]) check to see if we have a valid snake running through the matrix.
        # Each time we go down the matrix (i + 1) we go across the s1 string.
        # Each time we go right along the matrix (j + 1) we go across the s2 string.
        # This enables the dynamic programming concepts of overlapping sub-problems.
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[m][n]


if __name__ == '__main__':

    # Inputs and Expected Outputs
    s1_1 = "aabcc"
    s1_2 = "dbbca"
    s1_3 = "aadbbcbcac"
    expected_output_1 = True
    s2_1 = "aabcc"
    s2_2 = "dbbca"
    s2_3 = "aadbbbaccc"
    expected_output_2 = False
    s3_1 = ""
    s3_2 = ""
    s3_3 = ""
    expected_output_3 = True

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.interLeave(s1_1, s1_2, s1_3)
    test_2 = solution_2.interLeave(s2_1, s2_2, s2_3)
    test_3 = solution_3.interLeave(s3_1, s3_2, s3_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")