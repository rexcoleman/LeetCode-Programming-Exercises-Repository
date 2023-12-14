class Solution:
    def interLeave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False

        if m < n:
            return self.interLeave(s2, s1, s3)

        dp = [False] * (n + 1)
        dp[0] = True

        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            a = dp[0]
            for j in range(1, n + 1):
                b = dp[j]
                c = dp[j - 1]
                # 1'st term before or statement:
                # if the letters in s1 and s3 match and it was previously True then it stays true
                # This is analogous to moving down in the 2D matrix
                # 2'nd term after the or statement:
                # if the letters in s2 and s3 match and it the term before is true then turn this term true
                # This is analogous to moving to the right in a the 2D matrix
                # In both cases we use the -1 terms because we started with dp[0] = True to manage empty strings
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[n]




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

# a = dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1])
# b = s1[i - 1]
# c = s3[i + j - 1]
# d = (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
# e = s2[j - 1]
# f = s3[i + j - 1]