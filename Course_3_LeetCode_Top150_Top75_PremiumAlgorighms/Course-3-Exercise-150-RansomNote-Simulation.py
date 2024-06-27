class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # for each character, c, in the ransom note
        for c in ransomNote:
            # if there are none left of c in magazine, return false
            if c not in magazine:
                return False
            # find the index of the first occurrence of c in magazine
            location = magazine.index(c)
            # use splicing to make a new string with the characters
            # before "location," not including "location", after "location"
            magazine = magazine[:location] + magazine[location + 1:]
            print(magazine)
        # if we get this far we can successfully build the note
        return True





if __name__ == '__main__':

    solution = Solution()

    ransomNote1 = "a"
    magazine1 = "b"

    ransomNote2 = "aa"
    magazine2 = "ab"

    ransomNote3 = "aa"
    magazine3 = "aab"

    output1 = solution.canConstruct(ransomNote1, magazine1)
    output2 = solution.canConstruct(ransomNote2, magazine2)
    output3 = solution.canConstruct(ransomNote3, magazine3)

    print(f"Output1: {output1}")
    print(f"Output2: {output2}")
    print(f"Output3: {output3}")