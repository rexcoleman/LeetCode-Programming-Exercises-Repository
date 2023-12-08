class Solution:
    def trailingZeros(self, n: int) -> int:
        zero_count = 0
        for i in range(5, n + 1, 5):
            current = i
            while current % 5 == 0:
                zero_count += 1
                current //= 5
        return zero_count


if __name__ == '__main__':

    # Inputs and Expected Outputs
    n_1 = 3
    expected_output_1 = 0
    n_2 = 5
    expected_output_2 = 1
    n_3 = 0
    expected_output_3 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.trailingZeros(n_1)
    test_2 = solution_2.trailingZeros(n_2)
    test_3 = solution_3.trailingZeros(n_3)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3 Result: {test_3} \nExpected Result: {expected_output_3}")