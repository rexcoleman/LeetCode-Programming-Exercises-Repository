from collections import deque
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return[""]

        answer = []
        # Example: if n = 3 then F(3) = "(" + F(0) + ")" + F(2)  +
        # "(" + F(1) + ")" + F(1)  +  "(" + F(0) + ")" + F(2)
        # F(0) = "", F(1) = ()
        # Look at how the "left_count" argument translates to F(0, 1, 2, 3)
        # as left_count increments up
        for left_count in range(n):
            for left_string in self.generateParenthesis(left_count):
                for right_string in self.generateParenthesis(n - 1 - left_count):
                    answer.append('(' + left_string + ')' + right_string)

        return answer



if __name__ == '__main__':
    # Inputs and Expected Outputs
    n_1 = 3
    expected_output_1 = ["((()))","(()())","(())()","()(())","()()()"]
    n_2 = 1
    expected_output_2 = ["()"]
    n_3 = 2
    expected_output_3 = ["()()","(())"]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.generateParenthesis(n_1)
    test_2 = solution_2.generateParenthesis(n_2)
    test_3 = solution_3.generateParenthesis(n_3)


    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3 Result: {test_3} \nExpected Result: {expected_output_3}")
