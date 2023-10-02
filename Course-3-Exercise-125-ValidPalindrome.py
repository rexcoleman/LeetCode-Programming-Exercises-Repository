class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True








if __name__ == '__main__':

    solution = Solution()

    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    s3 = " "

    output1 = solution.isPalindrome(s1)
    output2 = solution.isPalindrome(s2)
    output3 = solution.isPalindrome(s3)

    print(f"Output1: {output1}")
    print(f"Output2: {output2}")
    print(f"Output3: {output3}")