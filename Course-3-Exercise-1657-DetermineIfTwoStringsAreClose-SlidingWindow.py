class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        pass


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

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.closeStrings(word1_1, word2_1)
    test_2 = solution_2.closeStrings(word1_2, word2_2)
    test_3 = solution_3.closeStrings(word1_3, word2_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")