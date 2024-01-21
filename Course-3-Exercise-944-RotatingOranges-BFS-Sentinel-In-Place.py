from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        # run the rotting process, by marking the rotten oranges with the timestamp
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        def runRottingProcess(timestamp):
            # flag to indicate if the rotting process should be continued
            to_be_continued = False
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == timestamp:
                        # current contaminated cell
                        for d in directions:
                            n_row, n_col = row + d[0], col + d[1]
                            if ROWS > n_row >= 0 and COLS > n_col >= 0:
                                if grid[n_row][n_col] == 1:
                                    # this fresh orange would be contaminated next
                                    grid[n_row][n_col] = timestamp + 1
                                    to_be_continued = True
            return to_be_continued

        timestamp = 2
        while runRottingProcess(timestamp):
            timestamp += 1

        # end of process, to check if there are still fresh oranges left
        for row in grid:
            for cell in row:
                if cell == 1:  # still got a fresh orange left
                    return -1

        # return elapsed minutes if no fresh orange left
        return timestamp - 2


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
    grid_4 = [[0]]
    expected_output_4 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    test_1 = solution_1.orangesRotting(grid_1)
    test_2 = solution_2.orangesRotting(grid_2)
    test_3 = solution_3.orangesRotting(grid_3)
    test_4 = solution_4.orangesRotting(grid_4)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
    print(f"\nTest 4 Output: {test_4} \nExpected Output: {expected_output_4}")