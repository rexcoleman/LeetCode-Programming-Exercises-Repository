class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 0 if not s or s.isspace() else len(s.split()[-1])


if __name__ == '__main__':

    solution = Solution()

    s1 = "Hello World"
    s2 = "   fly me   to   the moon       "
    s3 = "luffy is still joyboy"

    output1 = solution.lengthOfLastWord(s1)
    output2 = solution.lengthOfLastWord(s2)
    output3 = solution.lengthOfLastWord(s3)

    print(f"Answer for s1: {output1}")
    print(f"Answer for s2: {output2}")
    print(f"Answer for s3: {output3}")
