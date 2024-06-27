import math
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev_row = triangle[0]
        for row in range(1, len(triangle)):
            curr_row = []
            for col in range(row + 1):
                smallest_above = math.inf
                if col > 0:
                    smallest_above = prev_row[col - 1]
                if col < row:
                    smallest_above = min(smallest_above, prev_row[col])
                curr_row.append(triangle[row][col] + smallest_above)
            prev_row = curr_row
        return min(prev_row)




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
