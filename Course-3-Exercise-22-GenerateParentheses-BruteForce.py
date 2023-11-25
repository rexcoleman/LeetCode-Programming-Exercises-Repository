from collections import deque
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(p_string):
            left_count = 0
            for p in p_string:
                if p == '(':
                    left_count += 1
                else:
                    left_count -= 1
                if left_count < 0:
                    return False
            return left_count == 0

        answer = []
        queue = deque([""])
        while queue:
            cur_string = queue.popleft()
            # If the length of cur_string is 2 * n, add it to `answer` if it is valid.
            if len(cur_string) == 2 * n:
                if isValid(cur_string):
                    answer.append(cur_string)
                continue
            queue.append(cur_string + ')')
            queue.append(cur_string + '(')
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
