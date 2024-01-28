from functools import cache


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1_000_000_007

        # Handle base case scenarios
        if n <= 2:
            return n

        fCurrent, fPrevious, pCurrent = 2, 1, 1


        for k in range(3, n + 1):
            tmp = fCurrent
            fCurrent = (fCurrent + fPrevious + 2*pCurrent) % MOD
            pCurrent = (pCurrent + fPrevious) % MOD
            fPrevious = tmp
        return fCurrent


if __name__ == '__main__':

    # Inputs and Expected Outputs
    n_1 = 3
    expected_output_1 = 5
    n_2 = 1
    expected_output_2 = 1

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.numTilings(n_1)
    test_2 = solution_2.numTilings(n_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")