class Solution:
    def isArmstrong(self, n: int) -> bool:
        str_n = str(n)
        len_n = len(str_n)
        cumulative_sum = 0
        n_copy = n
        while n_copy > 0:
            temp = n_copy % 10
            cumulative_sum += temp ** len_n
            n_copy //= 10
        return cumulative_sum == n


if __name__ == '__main__':

    # Inputs and Expected Outputs
    n_1 = 153
    expected_output_1 = True
    n_2 = 123
    expected_output_2 = False

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.isArmstrong(n_1)
    test_2 = solution_2.isArmstrong(n_2)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")