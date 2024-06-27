import collections


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # check for obvious fail case
        if len(ransomNote) > len(magazine): return False

        # in Python, we can use the Counter class.  It does all the work that the
        # makeCountMap(...) function in our pseudocode did.
        letters = collections.Counter(magazine)
        print(f"letters {letters}")

        # for each character, c, in the ransom note
        for c in ransomNote:
            # if there are none of c left, return false
            if letters[c] <= 0:
                return False
            # remove one of c from the counter
            letters[c] -= 1
        # if we got this far, we can successfully build the note
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