class Solution:
    def trim_space(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # Remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1
        # Remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1
        # Reduce multiple spaces to a single space
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1
        return output

    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right -1

    def reverseEachWord(self, l: list) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            # go to the end of the word
            while end < n and l[end] != ' ':
                end += 1
            # Reverse the word
            self.reverse(l, start, end - 1)
            # Move to the next word
            start = end + 1
            end += 1

    def reverseWords(self, s: str) -> str:
        # Convert string to character array
        # and trim spaces at the same time
        l = self.trim_space(s)

        # Reverse the whole string
        self.reverse(l, 0, len(l) - 1)

        # Reverse each word
        self.reverseEachWord(l)

        return ''.join(l)

if __name__ == '__main__':

    # Inputs
    s1 = "the sky is blue"
    s2 = "  hello world  "
    s3 = "a good   example"

    # Run Tests

    # Run tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()

    test_1 = solution_1.reverseWords(s1)
    test_2 = solution_2.reverseWords(s2)
    test_3 = solution_3.reverseWords(s3)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")
    print(f"Test 3: {test_3}")
