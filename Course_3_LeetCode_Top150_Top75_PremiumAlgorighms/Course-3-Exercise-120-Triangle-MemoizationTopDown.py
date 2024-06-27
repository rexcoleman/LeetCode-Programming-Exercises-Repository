import math
from functools import lru_cache
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def min_path(row, col):
            path = triangle[row][col]
            if row < len(triangle) - 1:
                path += min(min_path(row + 1, col), min_path(row + 1, col + 1))
            return path

        return min_path(0, 0)


        below_row = triangle[-1]
        n = len(triangle)
        for row in reversed(range(n - 1)):
            curr_row = []
            for col in range(row + 1):
                smallest_below = min(below_row[col], below_row[col + 1])
                curr_row.append(triangle[row][col] + smallest_below)
            below_row = curr_row
        return below_row[0]


if __name__ == '__main__':
    # Inputs and Expected Outputs
    triangle_1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
    expected_output_1 = 11
    triangle_2 = [[-10]]
    expected_output_2 = -10


    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.minimumTotal(triangle_1)
    test_2 = solution_2.minimumTotal(triangle_2)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
