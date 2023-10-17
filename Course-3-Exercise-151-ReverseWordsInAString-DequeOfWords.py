from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        # Remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1
        # Remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1

        d, word = deque(), []
        # push word by word in front of deque
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))

        return ' '.join(d)

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
