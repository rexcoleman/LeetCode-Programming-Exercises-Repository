class Solution:

    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative

        for ch in s:
            if ch.isdigit():
                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':
                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand
                # Save the recently encountered '+' sign
                sign = 1
                # Reset operand
                operand = 0


            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':
                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':
                # Evaluate the expression to the left with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop()  # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop()  # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand


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
