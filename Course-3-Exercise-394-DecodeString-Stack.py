from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []; curNum = 0; curString = ''
        for char in s:
            if char == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif char == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + (num * curString)
            elif char.isdigit():  # curNum*10+int(c) is helpful in keep track of more than 1 digit number
                curNum = curNum * 10 + int(char)
            else:
                curString += char
        return curString


if __name__ == '__main__':
    # Inputs and Expected Outputs:
    s_1 = "3[a]2[bc]"
    expected_output_1 = "aaabcbc"
    s_2 = "3[a2[c]]"
    expected_output_2 = "accaccacc"
    s_3 = "2[abc]3[cd]ef"
    expected_output_3 = "abcabccdcdcdef"

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.decodeString(s_1)
    test_2 = solution_2.decodeString(s_2)
    test_3 = solution_3.decodeString(s_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
