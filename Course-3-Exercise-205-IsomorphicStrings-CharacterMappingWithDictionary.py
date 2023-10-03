class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping_s_t = {}
        mapping_t_s = {}

        for c1, c2 in zip(s, t):

            # Case 1: No mapping exists in either of the dictionaries
            if c1 not in mapping_s_t and c2 not in mapping_t_s:
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1

            # Case 2: Either mapping doesn't exist in one of the dictionaries or
            # mapping exists and it doesn't match in either dictionary or both
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False

        return True






if __name__ == '__main__':
    solution = Solution()

    s1 = "egg"
    t1 = "add"

    s2 = "foo"
    t2 = "bar"

    s3 = "paper"
    t3 = "title"

    output1 = solution.isIsomorphic(s1, t1)
    output2 = solution.isIsomorphic(s2, t2)
    output3 = solution.isIsomorphic(s3, t3)

    print(f"Output1: {output1}")
    print(f"Output2: {output2}")
    print(f"Output3: {output3}")