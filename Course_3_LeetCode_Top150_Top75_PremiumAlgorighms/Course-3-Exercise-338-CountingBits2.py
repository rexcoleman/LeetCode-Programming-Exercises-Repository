from math import log
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:

        def hammingWeight(i: int):
            count = 0
            while i:
                if i & 1:
                    bin_i = bin(i)
                    count += 1
                i = i >> 1
            return count

        ans = [0] * (n + 1)
        for i in range(n + 1):
            ans[i] = hammingWeight(i)
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
