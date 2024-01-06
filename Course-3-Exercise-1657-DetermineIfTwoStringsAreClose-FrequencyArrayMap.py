from collections import defaultdict
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        lst1 = [0] * 26
        lst2 = [0] * 26
        for i in word1:
            a = ord(i)
            lst1[ord(i) - 97] += 1
        for i in word2:
            lst2[ord(i) - 97] += 1
        for i in range(26):
            if (lst1[i] > 0 and lst2[i] == 0) or (lst1[i] == 0 and lst2[i] > 0):
                return False
        lst1.sort()
        lst2.sort()
        if lst1 == lst2:
            return True
        return False


if __name__ == '__main__':

    # Inputs and Expected Outputs:
    word1_1 = "abc"
    word2_1 = "bca"
    expected_output_1 = True
    word1_2 = "a"
    word2_2 = "aa"
    expected_output_2 = False
    word1_3 = "cabbba"
    word2_3 = "abbccc"
    expected_output_3 = True
    word1_4 = "abbzzca"
    word2_4 = "babzzcz"
    expected_output_4 = False

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    test_1 = solution_1.closeStrings(word1_1, word2_1)
    test_2 = solution_2.closeStrings(word1_2, word2_2)
    test_3 = solution_3.closeStrings(word1_3, word2_3)
    test_4 = solution_4.closeStrings(word1_4, word2_4)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
    print(f"\nTest 4 Output: {test_4} \nExpected Output: {expected_output_4}")