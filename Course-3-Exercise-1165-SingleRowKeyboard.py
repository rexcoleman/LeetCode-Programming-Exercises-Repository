class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {}
        for i in range(len(keyboard)):
            d[keyboard[i]] = i
        res = 0
        temp = 0
        for c in word:
            res += abs(d[c] - temp)
            temp = d[c]
        return res


if __name__ == '__main__':

    # Inputs and Expected Outputs
    keyboard_1 = "abcdefghijklmnopqrstuvwxyz"
    word_1 = "cba"
    expected_output_1 = 4
    keyboard_2 = "pqrstuvwxyzabcdefghijklmno"
    word_2 = "leetcode"
    expected_output_2 = 73

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.calculateTime(keyboard_1, word_1)
    test_2 = solution_2.calculateTime(keyboard_2, word_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")

