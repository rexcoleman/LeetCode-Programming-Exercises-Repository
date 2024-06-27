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

        queue, word = deque(), []
        while left <= right:
            # Word complete
            if s[left] == ' ' and word:
                queue.appendleft(''.join(word))
                word = []
            # Building word
            elif s[left] != ' ':
                word.append(s[left])
            # Manage blanks
            left += 1
        ' '.join(queue)



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