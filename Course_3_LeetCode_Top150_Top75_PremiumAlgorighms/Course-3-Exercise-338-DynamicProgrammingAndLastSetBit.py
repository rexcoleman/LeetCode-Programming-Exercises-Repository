from math import log
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            bin_a = bin(x)
            bin_b = bin(x-1)
            ans[x] = ans[x & (x - 1)] + 1
        return ans

if __name__ == '__main__':

    # Inputs and Expected Outputs
    n_1 = 2
    expected_output_1 = [0, 1, 1]
    n_2 = 5
    expected_output_2 = [0, 1, 1, 2, 1, 2]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.countBits(n_1)
    test_2 = solution_2.countBits(n_2)

    # Prnt Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 1 Output: {test_2} \nExpected Output: {expected_output_2}")
