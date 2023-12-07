class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            # Turn off the right-most bit
            m = bin(left)
            n = bin(right)
            o = bin(right - 1)
            right = right & (right - 1)
            n = bin(right)
        return left & right

if __name__ == '__main__':

    # Inputs and Expected Outputs
    left_1 = 5
    right_1 = 7
    expected_output_1 = 4
    left_2 = 0
    right_2 = 0
    expected_output_2 = 0
    left_3 = 1
    right_3 = 2147483647
    expected_output_3 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.rangeBitwiseAnd(left_1, right_1)
    test_2 = solution_2.rangeBitwiseAnd(left_2, right_2)
    test_3 = solution_3.rangeBitwiseAnd(left_3, right_3)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3 Result: {test_3} \nExpected Result: {expected_output_3}")