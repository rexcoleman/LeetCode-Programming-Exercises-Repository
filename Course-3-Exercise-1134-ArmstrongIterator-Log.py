import math


class Solution:
    def isArmstrong(self, n: int) -> bool:
        original, new = n, 0
        k = math.floor(math.log10(n)) + 1

        while n:
            n, d = divmod(n, 10)
            new += d**k

        return new == original


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