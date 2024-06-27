class Solution:

    def evaluate_expr(self, stack):
        # If stack is empty or the expression starts with
        # a symbol, then append 0 to the stack.
        # i.e. [1, '-', 2, '-'] becomes [1, '-', 2, '-', 0]
        if not stack or type(stack[-1]) == str:
            stack.append(0)

        res = stack.pop()

        # Evaluate the expression till we get corresponding ')'
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()
        return res

    def calculate(self, s: str) -> int:
        stack = []
        n, operand = 0, 0

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch.isdigit():
                # Forming the operand - in reverse order.
                operand = (10 ** n * int(ch)) + operand
                n += 1

            elif ch != " ":
                if n:
                    # Save the operand on the stack
                    # As we encounter some non-digit.
                    stack.append(operand)
                    n, operand = 0, 0
                if ch == "(":
                    res = self.evaluate_expr(stack)
                    stack.pop()

                    # Append the evaluated result to the stack.
                    # This result could be of a sub-expression within the parenthesis.

                    stack.append(res)

                # For other non-digits just push onto the stack.
                else:
                    stack.append(ch)

        # Push the last operand to stack, if any.
        if n:
            stack.append(operand)
        # Evaluate any leftovers in the stack.
        return self.evaluate_expr(stack)





if __name__ == '__main__':

    # Inputs and Expected Outputs
    s_1 = "1 + 1"
    expected_output_1 = 2
    s_2 = "2 - 1 + 2"
    expected_output_2 = 3
    s_3 = "(1+(4+5+2)-3)+(6+8)"
    expected_output_3 = 23

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.calculate(s_1)
    test_2 = solution_2.calculate(s_2)
    test_3 = solution_3.calculate(s_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
