class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = len(s)
        length = 0

        while p > 0:
            p -= 1
            # we're in the middle of the last word
            if s[p] != ' ':
                length += 1
            # here is the end of last word
            elif length > 0:
                return length

        return length










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
