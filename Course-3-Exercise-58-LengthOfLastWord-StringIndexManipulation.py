
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = len(s) - 1

        # trim end spaces
        while p >= 0 and s[p] == " ":
            p -= 1
        print(p)

        # compute length of the last word

        length = 0

        while p >= 0 and s[p] != " ":
            p -= 1
            length += 1

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
