class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        str1 = sorted(s)
        str2 = sorted(t)

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False

        return True





if __name__ == '__main__':

    solution = Solution()

    s1 = "anagram"
    t1 = "nagaram"
    s2 = "rat"
    t2 = "car"

    output1 = solution.isAnagram(s1, t1)
    output2 = solution.isAnagram(s2, t2)

    print(f"Output1: {output1}")
    print(f"Output2: {output2}")