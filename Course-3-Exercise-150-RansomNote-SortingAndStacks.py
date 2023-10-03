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

        # Reverse sort the magazine.  In Python we simply
        # treat the list as a stack.
        ransomNote = sorted(ransomNote, reverse=True)
        magazine = sorted(magazine, reverse=True)

        # While there are letters left on both stacks
        while ransomNote and magazine:
            # If the tops are the same, pop both because we found a match
            if ransomNote[-1] == magazine[-1]:
                ransomNote.pop()
                magazine.pop()
            # If magazine's top is earlier in the alphabet, we should remove that
            # character of magazine because we definitely won't need that letter
            elif magazine[-1] < ransomNote[-1]:
                magazine.pop()
            # Otherwise it is impossible for the top of ransomNote to be in the magazine.
            else:
                return False
        # Return true if the entire ransomNote was build.
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