class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        map_char = {}
        map_word = {}

        words = s.split(' ')
        print(words)

        # Test for length match.  Return false if not true
        if len(words) != len(pattern):
            return False


        for c, w in zip(pattern, words):
            # This is the case where we do not have a letter to word mapping
            if c not in map_char:
                # Test if we have already mapped a word to a different letter.
                # Return false if true
                # Otherwise create both mappings
                if w in map_word:
                    return False
                else:
                    map_char[c] = w
                    map_word[w] = c
            # This is the case where we already have a letter to word mapping
            else:
                # Tests if letter to word mapping matches word to letter mapping
                # Return false if not a match
                if map_char[c] != w:
                    return False
        # if we get to the end then return true
        return True





if __name__ == "__main__":

    solution = Solution()

    pattern1 = "abba"
    s1 = "dog cat cat dog"

    pattern2 = "abba"
    s2 = "dog cat cat fish"

    pattern3 = "aaaa"
    s3 = "dog cat cat dog"

    outcome1 = solution.wordPattern(pattern1, s1)
    outcome2 = solution.wordPattern(pattern2, s2)
    outcome3 = solution.wordPattern(pattern3, s3)

    print(f"Outcome1: {outcome1}")
    print(f"Outcome2: {outcome2}")
    print(f"Outcome3: {outcome3}")