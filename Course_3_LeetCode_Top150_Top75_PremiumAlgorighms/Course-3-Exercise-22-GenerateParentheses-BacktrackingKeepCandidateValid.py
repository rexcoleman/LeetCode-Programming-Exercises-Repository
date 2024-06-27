from collections import deque
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backtracking(cur_string, left_count, right_count):
            if len(cur_string) == 2 * n:
                answer.append(''.join(cur_string))
                return
            if left_count < n:
                cur_string.append('(')
                backtracking(cur_string, left_count + 1, right_count)
                cur_string.pop()
            if right_count < left_count:
                cur_string.append(')')
                backtracking(cur_string, left_count, right_count + 1)
                cur_string.pop()
        backtracking([], 0, 0)
        return answer




if __name__ == '__main__':
    # Inputs and Expected Outputs
    n_1 = 3
    expected_output_1 = ["((()))","(()())","(())()","()(())","()()()"]
    n_2 = 1
    expected_output_2 = ["()"]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.generateParenthesis(n_1)
    test_2 = solution_2.generateParenthesis(n_2)


    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
