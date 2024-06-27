from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        min_dist = float('inf')
        nsew = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        steps = 0
        queue = deque([(entrance[0], entrance[1], steps)])
        rows = len(maze)
        cols = len(maze[0])
        entrance_row = entrance[0]
        entrance_col = entrance[1]

        # Corner cases
        if entrance_row == 0 or entrance_row == (rows - 1) or entrance_col == 0 or entrance_col == (cols - 1):
            maze[entrance_row][entrance_col] = 'a'

        # BFS
        while queue:
            row, col, steps = queue.popleft()
            maze[row][col] = 'a'

            for direction in nsew:
                curr_row = row + direction[0]
                curr_col = col + direction[1]

                if curr_row < 0 or curr_row >= rows or curr_col < 0 or curr_col >= cols:
                    continue

                elif maze[curr_row][curr_col] == '+' or maze[curr_row][curr_col] == 'a':
                    continue
                elif curr_row <= 0 or curr_row >= rows - 1 or curr_col <= 0 or curr_col >= cols - 1:
                    steps += 1
                    min_dist = min(min_dist, steps)
                else:
                    queue.append((curr_row, curr_col, steps + 1))
        return -1 if min_dist == float('inf') else min_dist




if __name__ == '__main__':

    # Inputs and Expected Outputs
    maze_1 = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
    entrance_1 = [1, 2]
    expected_output_1 = 1
    maze_2 = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
    entrance_2 = [1, 0]
    expected_output_2 = 2
    maze_3 = [[".", "+"]]
    entrance_3 = [0, 0]
    expected_output_3 = -1
    maze_4 = [
        ["+", ".", "+", "+", "+", "+", "+"],
        ["+", ".", "+", ".", ".", ".", "+"],
        ["+", ".", "+", ".", "+", ".", "+"],
        ["+", ".", ".", ".", ".", ".", "+"],
        ["+", "+", "+", "+", ".", "+", "."]
    ]
    entrance_4 = [0, 1]
    expected_output_4 = 7

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    test_1 = solution_1.nearestExit(maze_1, entrance_1)
    test_2 = solution_2.nearestExit(maze_2, entrance_2)
    test_3 = solution_3.nearestExit(maze_3, entrance_3)
    test_4 = solution_4.nearestExit(maze_4, entrance_4)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
    print(f"\nTest 4 Output: {test_4} \nExpected Output: {expected_output_4}")
