class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == haystack:
            return 0

        n = len(needle)
        h = len(haystack)

        for i in range(h - n + 1):
            if haystack[i:i+n] == needle:
                return i
            i += 1
        return -1



if __name__ == '__main__':

    haystack1 = "sadbutsad"
    needle1 = "sad"
    haystack2 = "leetcode"
    needle2 = "leeto"
    haystack3 = "mississippi"
    needle3 = "a"
    haystack4 = "a"
    needle4 = "a"
    haystack5 = "abc"
    needle5 = "c"

    solution = Solution()

    output1 = solution.strStr(haystack1, needle1)
    output2 = solution.strStr(haystack2, needle2)
    output3 = solution.strStr(haystack3, needle3)
    output4 = solution.strStr(haystack4, needle4)
    output5 = solution.strStr(haystack5, needle5)

    print(f"Output1: {output1}")
    print(f"Output2: {output2}")
    print(f"Output3: {output3}")
    print(f"Output4: {output4}")
    print(f"Output5: {output5}")


