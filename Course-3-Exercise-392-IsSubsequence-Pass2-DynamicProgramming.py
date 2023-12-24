import bisect
from collections import defaultdict


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        source_len, target_len = len(s), len(t)

        # the source string is empty
        if source_len == 0:
            return True

        # matrix to store the history of matches/deletions
        dp = [ [0] * (target_len + 1) for _ in range(source_len + 1) ]

        # DP compute, we fill the matrix column by column, bottom up
        for col in range(1, target_len + 1):
            for row in range(1, source_len + 1):
                if s[row - 1] == t[col - 1]:
                    # found another match
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    # retrieve the maximal result from previous prefixes
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])

            # check if we can consume the entire source string,
            # with the current prefix of the target string.
            if dp[source_len][col] == source_len:
                return True

        return False


if __name__ == '__main__':

    # Inputs and Expected Outputs:
    s1 = "bbbac"
    t1 = "ahbbbgdc"
    expected_output_1 = False
    s2 = "axc"
    t2 = "ahbgdc"
    expected_output_2 = False
    s3 = "acb"
    t3 = "ahbgdc"
    expected_output_3 = False
    s4 = "abc"
    t4 = "ahbgdc"
    expected_output_4 = True


    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    test_1 = solution_1.isSubsequence(s1, t1)
    test_2 = solution_2.isSubsequence(s2, t2)
    test_3 = solution_3.isSubsequence(s3, t3)
    test_4 = solution_4.isSubsequence(s4, t4)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
    print(f"\nTest 4 Output: {test_4} \nExpected Output: {expected_output_4}")