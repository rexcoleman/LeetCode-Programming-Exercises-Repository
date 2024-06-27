class Solution(object):
    def transfromString(self, s: str):
        index_mapping = {}
        new_str = []
        for i, c in enumerate(s):
            if c not in index_mapping:
                index_mapping[c] = i
            new_str.append(str(index_mapping[c]))

        return " ".join(new_str)


    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.transfromString(s) == self.transfromString(t)






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