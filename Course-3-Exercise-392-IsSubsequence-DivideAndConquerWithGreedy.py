class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        def rec_isSubsequence(left_index, right_index):
            # base cases
            if left_index == LEFT_BOUND:
                return True
            if right_index == RIGHT_BOUND:
                return False

            # consume both strings or just the target string
            if s[left_index] == t[right_index]:
                left_index += 1
            right_index += 1

            return rec_isSubsequence(left_index, right_index)

        return rec_isSubsequence(0, 0)






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