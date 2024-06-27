class Solution:
    def binaryExp(self, x: float, n: int) -> float:
        # Base case, to stop recursive calls.
        if n == 0:
            return 1

        # Handle case where, n < 0.
        if n < 0:
            return 1.0 / self.binaryExp(x, -1 * n)

        # Perform Binary Exponentiation.
        # If 'n' is odd we perform Binary Exponentiation on 'n - 1' and multiply result with 'x'.
        if n % 2 == 1:
            return x * self.binaryExp(x * x, (n - 1) // 2)
        # Otherwise we calculate result by performing Binary Exponentiation on 'n'.
        else:
            return self.binaryExp(x * x, n // 2)

    def myPow(self, x: float, n: int) -> float:
        return self.binaryExp(x, n)


if __name__ == '__main__':

    # Inputs and Expected Outputs
    x_1 = 2.00000
    n_1 = 10
    expected_output_1 = 1024.00000
    x_2 = 2.10000
    n_2 = 3
    expected_output_2 = 9.26100
    x_3 = 2.00000
    n_3 = -2
    expected_output_3 = 0.25000

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.binaryExp(x_1, n_1)
    test_2 = solution_2.binaryExp(x_2, n_2)
    test_3 = solution_3.binaryExp(x_3, n_3)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3 Result: {test_3} \nExpected Result: {expected_output_3}")

