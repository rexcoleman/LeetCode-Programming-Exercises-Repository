import bisect
from collections import defaultdict


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letter_indices_table = defaultdict(list)
        for index, letter in enumerate(t):
            letter_indices_table[letter].append(index)
            print(f"letter_indices_table {letter_indices_table}")

        curr_match_index = -1
        for letter in s:
            if letter not in letter_indices_table:
                # no match at all, exit early
                return False

            # greedy match with binary search
            indices_list = letter_indices_table[letter]
            print(f"len_indices_list {len(indices_list)}")
            print(f"indices_list {indices_list}")
            print(f"curr_match_index {curr_match_index}")
            match_index = bisect.bisect_right(indices_list, curr_match_index)
            print(f"match_index {match_index}")
            if match_index != len(indices_list):
                curr_match_index  = indices_list[match_index]
            else:
                # no suitable match found, exit early
                return False
        return True





if __name__ == '__main__':

    solution = Solution()

    s1 = "abcd"
    t1 = "ahbgdc"

    s2 = s = "axc"
    t2 = "ahbgdc"

    output1 = solution.isSubsequence(s1, t1)
    output2 = solution.isSubsequence(s2, t2)

    print(f"Output1: {output1}")
    print(f"Output2: {output2}")