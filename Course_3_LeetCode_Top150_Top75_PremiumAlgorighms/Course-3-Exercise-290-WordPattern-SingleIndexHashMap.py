class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        map_index = {}
        words = s.split()

        # quick test to filter out length mismatch case
        if len(pattern) != len(words):
            return False

        # one loop to iterate through both pattern and words using i
        # Time complexity O(N+M) where N represents length of s and
        # M represents length of pattern
        for i in range(len(words)):

            c = pattern[i]
            w = words[i]

            # format letters and words to account for case where words are characters
            # e.g. pattern = "abba" and words = "b a a b" would return false when it should be true
            char_key = 'char_{}'.format(c)
            char_word = 'word_{}'.format(w)

            # add index values if key/pattern letter not in dictionary
            if char_key not in map_index:
                map_index[char_key] = i

            # add index values if word not in dictionary
            if char_word not in map_index:
                map_index[char_word] = i

            # Search for index match. If not a match, return false.
            if map_index[char_key] != map_index[char_word]:
                return False
        # If we get to the end return true
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