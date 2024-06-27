from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = defaultdict(int)

        if len(s) != len(t):
            return False

        # Count the frequency of characters in string s
        for x in s:
            count[x] += 1
            print(count)

        # Decrement the frequency of characters in string t
        for x in t:
            count[x] -= 1
            print(count)

        # Check if any character has non-zero frequency
        for val in count.values():
            if val != 0:
                return False

        print(count)
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