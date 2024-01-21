from collections import deque
from typing import List


from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        next_level = deque()

        # Step 1). build the initial set of rotten oranges
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    next_level.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1


        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while next_level:
            curr_level = next_level
            next_level = deque()

            while curr_level:
                row, col = curr_level.popleft()
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would be contaminated
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            # this orange would then contaminate other oranges
                            next_level.append((neighbor_row, neighbor_col))
            minutes_elapsed += 1


        # return elapsed minutes if no fresh orange left
        return minutes_elapsed if fresh_oranges == 0 else -1


if __name__ == '__main__':

    # Inputs and Expected Outputs
    grid_1 = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    expected_output_1 = 4
    grid_2 = [
        [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1]
    ]
    expected_output_2 = -1
    grid_3 = [[0, 2]]
    expected_output_3 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.orangesRotting(grid_1)
    test_2 = solution_2.orangesRotting(grid_2)
    test_3 = solution_3.orangesRotting(grid_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")