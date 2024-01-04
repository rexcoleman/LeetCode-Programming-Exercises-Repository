from collections import deque
from typing import List


class Solution:

    # Remove leading and trailing spaces
    def trimSpaces(self, s) -> list:
        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1
        return output

    # Reverse whole string
    def reverse(self, l: List, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    # Reverse individual words
    def reverseEachWord(self, l: List) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            while end < n and l[end] != ' ':
                end += 1
            self.reverse(l, start, end - 1)
            start = end + 1
            end += 1

    def reverseWords(self, s: str) -> str:

        # Convert string to character array
        # and trim spaces at the same time
        l = self.trimSpaces(s)

        # Reverse the whole string
        self.reverse(l, 0, len(l) - 1)

        # Reverse each word
        self.reverseEachWord(l)





if __name__ == '__main__':

    # Inputs and Expected Outputs
    s_1 = "the sky is blue"
    expected_output_1 = "blue is sky the"
    s_2 = "  hello world  "
    expected_output_2 = "world hello"
    s_3 = "a good   example"
    expected_output_3 = "example good a"

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.reverseWords(s_1)
    test_2 = solution_2.reverseWords(s_2)
    test_3 = solution_3.reverseWords(s_3)

    # Prnt Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")