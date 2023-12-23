class Solution:
    def reverseVowels(self, s: str) -> str:
        # Create hashset to test vowels condition.
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        start, end = 0, len(s) - 1
        string_update = list(s)
        while start < end:
            while string_update[start] not in vowels and start < end:
                start += 1
            while string_update[end] not in vowels and start < end:
                end -= 1
            if start < end:
                string_update[start], string_update[end] = string_update[end], string_update[start]
            start += 1
            end -= 1

        return "".join(string_update)


if __name__ == '__main__':

    # Inputs and Expected Outputs
    s_1 = "hello"
    expected_output_1 = "holle"
    s_2 = "leetcode"
    expected_output_2 = "leotcede"

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.reverseVowels(s_1)
    test_2 = solution_1.reverseVowels(s_2)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")