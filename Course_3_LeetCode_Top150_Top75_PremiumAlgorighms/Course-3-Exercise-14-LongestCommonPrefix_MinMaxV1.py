class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        m = min(strs)
        M = max(strs)
        i = 0
        for i in range(min(len(m), len(M))):
            if m[i] != M[i]:
                break
            else: i += 1
        return m[:i]


if __name__ == '__main__':

    solution = Solution()

    s1 = ["flower","flow","flight"]
    s2 = ["dog","racecar","car"]

    output1 = solution.longestCommonPrefix(s1)
    output2 = solution.longestCommonPrefix(s2)

    print(f"Output 1: {output1}")
    print(f"Output 2: {output2}")