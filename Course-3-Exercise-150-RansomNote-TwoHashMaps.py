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
        magazine_counts = collections.Counter(magazine)
        ransom_note_counts = collections.Counter(ransomNote)
        # print(f"magazine_counts {magazine_counts}")
        # print(f"ransom_note_counts {ransom_note_counts}")
        # print(f"magazine_counts_items {magazine_counts.items}")
        # print(f"ransom_note_counts_items {ransom_note_counts.items()}")

        # for each unique character in the ransom note
        for char, count in ransom_note_counts.items():
            # check that the count of char in the magazine is equal
            # or higher than the count in the ransom note.
            magazine_count = magazine_counts[char]
            if magazine_count < count:
                return False

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