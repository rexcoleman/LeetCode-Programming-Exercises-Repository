class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        str1, str2 = min(strs), max(strs)
        i = 0
        while i < len(str1):
            if str1[i] != str2[i]:
                str1 = str1[:i]
            i += 1
        return str1



if __name__ == '__main__':

    solution = Solution()

    s1 = ["flower","flow","flight"]
    s2 = ["dog","racecar","car"]

    output1 = solution.longestCommonPrefix(s1)
    output2 = solution.longestCommonPrefix(s2)

    print(f"Output 1: {output1}")
    print(f"Output 2: {output2}")