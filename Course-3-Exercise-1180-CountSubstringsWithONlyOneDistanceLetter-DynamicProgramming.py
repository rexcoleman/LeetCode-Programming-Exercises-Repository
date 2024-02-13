class Solution:
    def countLetters(self, s: str) -> int:
        total = 1
        substrings = [0] * len(s)
        substrings[0] = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                substrings[i] = substrings[i-1] + 1
            else:
                substrings[i] = 1
            total += substrings[i]

        return total


if __name__ == '__main__':

    # Inputs and Expected Outputs
    s_1 = "aaaba"
    expected_output_1 = 8
    s_2 = "aaaaaaaaaa"
    expected_output_2 = 55

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.countLetters(s_1)
    test_2 = solution_2.countLetters(s_2)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")