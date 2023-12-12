class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start: start + length]

        return ""


if __name__ == '__main__':

    # Inputs and Expected Outputs
    s_1 = "babad"
    expected_output_1 =  "bab"
    s_2 = "cbbd"
    expected_output_2 = "bb"

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.longestPalindrome(s_1)
    test_2 = solution_2.longestPalindrome(s_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")