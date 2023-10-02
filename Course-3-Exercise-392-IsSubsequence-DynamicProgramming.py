import bisect
from collections import defaultdict


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        source_len, target_len = len(s), len(t)

        # the source string is empty
        if source_len == 0:
            return True

        # matrix to store the history of matches/deletions
        dp = [ [0] * (target_len + 1) for _ in range(source_len + 1) ]
        print(dp)

        # DP compute, we fill the matrix column by column, bottom up
        for col in range(1, target_len + 1):
            for row in range(1, source_len + 1):
                if s[row - 1] == t[col - 1]:
                    # find another match
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    # retrieve the maximal result from the previous prefixes
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])

            # check if we can consume the entire source string
            # with the current prefix of the target string
            if dp[source_len][col] == source_len:
                return True
        return False




if __name__ == '__main__':

    solution = Solution()

    s1 = "abc"
    t1 = "ahbgdc"

    s2 = s = "axc"
    t2 = "ahbgdc"

    output1 = solution.isSubsequence(s1, t1)
    output2 = solution.isSubsequence(s2, t2)

    print(f"Output1: {output1}")
    print(f"Output2: {output2}")