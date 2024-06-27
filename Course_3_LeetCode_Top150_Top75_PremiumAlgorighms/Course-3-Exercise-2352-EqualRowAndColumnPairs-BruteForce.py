from collections import defaultdict
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)

        # Check each row r against each column c.
        for r in range(n):
            for c in range(n):
                match = True

                # Iterate over row r and column c.
                for i in range(n):
                    if grid[r][i] != grid[i][c]:
                        match = False
                        break

                # If row r equals column c, increment count by 1.
                count += int(match)

        return count




if __name__ == '__main__':

    # Inputs and Expected Outputs:
    grid_1 = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    expected_output_1 = 1
    grid_2 = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    expected_output_2 = 3

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.equalPairs(grid_1)
    test_2 = solution_2.equalPairs(grid_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
