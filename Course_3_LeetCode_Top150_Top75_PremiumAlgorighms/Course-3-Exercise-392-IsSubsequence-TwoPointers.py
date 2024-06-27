class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)
        p_left = p_right = 0

        while p_left < LEFT_BOUND and p_right < RIGHT_BOUND:
            # move both pointers or just the right pointer
            if s[p_left] == t[p_right]:
                p_left += 1
            p_right += 1
        return p_left == LEFT_BOUND










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