class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Build the window of size k, count the number of vowels it contains.
        count = 0
        for i in range(k):
            count += int(s[i] in vowels)
        answer = count

        # Slide the window to the right, focus on the added character and the
        # removed character and update "count". Record the largest "count".
        for i in range(k, len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i - k] in vowels)
            answer = max(answer, count)

        return answer


if __name__ == '__main__':

    # Inputs and Expected Outputs:
    s_1 = "abciiidef"
    k_1 = 3
    expected_output_1 = 3
    s_2 = "aeiou"
    k_2 = 2
    expected_output_2 = 2
    s_3 = "leetcode"
    k_3 = 3
    expected_output_3 = 2

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.maxVowels(s_1, k_1)
    test_2 = solution_2.maxVowels(s_2, k_2)
    test_3 = solution_3.maxVowels(s_3, k_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")