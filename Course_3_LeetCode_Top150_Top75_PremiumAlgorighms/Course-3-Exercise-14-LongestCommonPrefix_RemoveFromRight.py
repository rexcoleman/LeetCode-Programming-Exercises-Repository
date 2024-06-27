class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre = strs[0]

        for i in strs:
            while not i.startswith(pre):
                pre = pre[:-1]

        return pre


if __name__ == '__main__':

    solution = Solution()

    s1 = ["flower","flow","flight"]
    s2 = ["dog","racecar","car"]

    output1 = solution.longestCommonPrefix(s1)
    output2 = solution.longestCommonPrefix(s2)

    print(f"Output 1: {output1}")
    print(f"Output 2: {output2}")