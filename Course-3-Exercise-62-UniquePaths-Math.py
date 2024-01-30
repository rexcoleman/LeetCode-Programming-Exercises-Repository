from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)


if __name__ == '__main__':

    # Inputs and Expected Outputs
    m_1 = 3
    n_1 = 7
    expected_output_1 = 28
    m_2 = 3
    n_2 = 2
    expected_output_2 = 3

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.uniquePaths(m_1, n_1)
    test_2 = solution_2.uniquePaths(m_2, n_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")