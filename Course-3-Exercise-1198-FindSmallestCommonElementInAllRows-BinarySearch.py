from collections import defaultdict
from typing import List


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        for j in range(n):
            cur = 1
            for i in range(1, m):
                lo, hi = 0, n - 1
                # in this binary search we may not find a match.  In that case we need a wqy to move
                # on to the next row.
                # This is controlled for when the whole list is greater than our target value: i) +1 in mid calc
                # ensures that mid is never zero and therefore hi is >= 0. This way when lo == hi at the zero index
                # we can exit the while loop.  Then we can test if they are equal.
                # On the upper end we do lo = mid.  Because mid leans up to high
                # mid will natrually become hi but not avove hi
                while lo < hi:
                    mid = (lo + hi + 1) // 2
                    a = mat[i][mid]
                    b = mat[0][j]
                    if mat[i][mid] > mat[0][j]:
                        hi = mid - 1
                    else:
                        lo = mid
                if mat[i][lo] == mat[0][j]:
                    cur += 1
            if cur == m:
                return mat[0][j]
        return -1


if __name__ == '__main__':
    # Inputs and Expected Outputs
    mat_1 = [[1, 2, 3, 4, 20], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]
    expected_output_1 = 5
    mat_2 = [[1, 2, 3], [2, 3, 4], [2, 3, 5]]
    expected_output_2 = 2

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.smallestCommonElement(mat_1)
    test_2 = solution_2.smallestCommonElement(mat_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")