from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b,
        }

        stack = []

        for token in tokens:
            if token in operations:
                number_2 = stack.pop()
                number_1 = stack.pop()
                operation = operations[token]
                stack.append(operation(number_1, number_2))
            else:
                stack.append(int(token))

        return stack.pop()





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