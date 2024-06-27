class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            left = i
            right = j
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        ans = [0, 0]

        for i in range(len(s)):
            odd_length = expand(i, i)
            if odd_length > ans[1] - ans[0] + 1:
                dist = odd_length // 2
                ans = [i - dist, i + dist]

            even_length = expand(i, i + 1)
            if even_length > ans[1] - ans[0] + 1:
                dist = (even_length // 2) - 1
                ans = [i - dist, i + 1 + dist]

        i, j = ans
        return s[i: j + 1]


if __name__ == '__main__':

    # Inputs and Expected Outputs
    s_1 = "babad"
    expected_output_1 =  "bab"
    s_2 = "cbbd"
    expected_output_2 = "bb"
    s_3 = "aaaaa"
    expected_output_3 = "aaaaa"

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.longestPalindrome(s_1)
    test_2 = solution_2.longestPalindrome(s_2)
    test_3 = solution_3.longestPalindrome(s_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")