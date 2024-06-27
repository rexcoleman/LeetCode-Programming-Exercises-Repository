class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        len_s = len(s)
        for i in range(len_s):
            stack.append(s[i])
            if stack[-1] == '*':
                stack.pop()
                stack.pop()
        return ''.join(stack)


if __name__ == '__main__':

    # Inputs and Expected Outputs:
    s_1 = "leet**cod*e"
    expected_output_1 = "lecoe"
    s_2 = "erase*****"
    expected_output_2 = ""

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.removeStars(s_1)
    test_2 = solution_2.removeStars(s_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
