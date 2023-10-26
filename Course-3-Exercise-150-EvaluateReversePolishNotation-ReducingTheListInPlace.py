from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }

        current_position = 0

        while len(tokens) > 1:
            # Move the current position pointer to the next operator.
            while tokens[current_position] not in "+-/*":
                current_position += 1

            # Extract the operator and numbers from the list
            operator = tokens[current_position]
            number_1 = int(tokens[current_position - 2])
            number_2 = int(tokens[current_position - 1])

            # Calculate the result to overwrite the operator with
            operation = operations[operator]
            tokens[current_position] = operation(number_1, number_2)

            # Remove the numbers and move the pointer to the position
            # after the new number we just added
            tokens.pop(current_position - 2)
            tokens.pop(current_position - 2)
            current_position -= 1

        return tokens[0]




if __name__ == '__main__':

    # Inputs
    tokens_1 = ["2", "1", "+", "3", "*"]
    tokens_2 = ["4", "13", "5", "/", "+"]
    tokens_3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

    # Run tests

    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()

    test_1 = solution_1.evalRPN(tokens_1)
    test_2 = solution_2.evalRPN(tokens_2)
    test_3 = solution_3.evalRPN(tokens_3)

    print(f"Test 1: {test_1}, Expected Result: 9")
    print(f"Test 1: {test_2}, Expected Result: 6")
    print(f"Test 1: {test_3}, Expected Result: 22")