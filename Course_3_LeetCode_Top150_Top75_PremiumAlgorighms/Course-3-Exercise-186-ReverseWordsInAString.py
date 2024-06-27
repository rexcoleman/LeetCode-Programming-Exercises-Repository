from typing import List


class Solution:

    def reverseString(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1

    def reverseEachWord(self, s: list):
        n = len(s)
        start = end = 0

        while start < n:
            # go to the end of the word
            while end < n and s[end] != ' ':
                end += 1
            # reverse the word
            self.reverseString(s, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1

    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # reverse the whole string
        self.reverseString(s, 0, len(s) - 1)

        # reverse each word
        self.reverseEachWord(s)


if __name__ == '__main__':

    # Inputs and Expected Outputs
    s_1 = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
    expected_output_1 = ["b", "l", "u", "e", " ", "i", "s", " ", "s", "k", "y", " ", "t", "h", "e"]
    s_2 = ["a"]
    expected_output_2 = ["a"]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.reverseWords(s_1)
    test_2 = solution_2.reverseWords(s_2)
    print(f"\nTest 1 Output: {s_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {s_2} \nExpected Output: {expected_output_2}")