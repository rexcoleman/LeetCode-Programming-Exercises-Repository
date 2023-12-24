import bisect
from collections import defaultdict


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        letter_indices_table = defaultdict(list)
        for index, letter in enumerate(t):
            letter_indices_table[letter].append(index)

        curr_match_index = -1
        for letter in s:
            if letter not in letter_indices_table:
                return False  # no match at all, early exit

            # greedy match with binary search
            # curr_match_index tracks the algorithms progression across the t-string
            # if match_index == len(indices_list) this means that the curr_match_index
            # is greater than all the indices for the letter in the s-list
            # This tool is used in binary_search implementations as it reduces the search space
            indices_list = letter_indices_table[letter]
            match_index = bisect.bisect_right(indices_list, curr_match_index)
            if match_index != len(indices_list):
                curr_match_index = indices_list[match_index]
            else:
                return False  # no suitable match found, early exit

        return True


if __name__ == '__main__':

    # Inputs and Expected Outputs:
    s1 = "bbbac"
    t1 = "ahbbbgdc"
    expected_output_1 = False
    s2 = "axc"
    t2 = "ahbgdc"
    expected_output_2 = False
    s3 = "acb"
    t3 = "ahbgdc"
    expected_output_3 = False
    s4 = "abc"
    t4 = "ahbgdc"
    expected_output_4 = True


    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    test_1 = solution_1.isSubsequence(s1, t1)
    test_2 = solution_2.isSubsequence(s2, t2)
    test_3 = solution_3.isSubsequence(s3, t3)
    test_4 = solution_4.isSubsequence(s4, t4)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
    print(f"\nTest 4 Output: {test_4} \nExpected Output: {expected_output_4}")