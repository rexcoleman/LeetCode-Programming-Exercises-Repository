class Solution:
    def confusingNumber(self, n: int) -> bool:
        confusing_dict = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6
        }
        start_num = n
        final_num = 0
        while start_num > 0:
            res = start_num % 10
            if res not in confusing_dict:
                return False
            else:
                final_num = final_num * 10 + confusing_dict[res]
                start_num //= 10
        return final_num != n


if __name__ == '__main__':

    # Inputs and Expected Outputs
    n_1 = 6
    expected_output_1 = True
    n_2 = 89
    expected_output_2 = True
    n_3 = 11
    expected_output_3 = False

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.confusingNumber(n_1)
    test_2 = solution_2.confusingNumber(n_2)
    test_3 = solution_3.confusingNumber(n_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")