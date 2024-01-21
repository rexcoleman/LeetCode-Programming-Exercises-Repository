from collections import deque
from typing import List


from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        rows, cols = len(maze), len(maze[0])
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))

        # Mark the entrance as visited since its not a exit.
        start_row, start_col = entrance
        maze[start_row][start_col] = '+'

        # Start BFS from the entrance, and use a queue `queue` to store all
        # the cells to be visited.
        queue = deque()
        queue.append([start_row, start_col, 0])


        while queue:
            curr_row, curr_col, curr_distance = queue.popleft()

            # For the current cell, check its four neighbor cells.
            for d in dirs:
                next_row = curr_row + d[0]
                next_col = curr_col + d[1]

                # If there exists an unvisited empty neighbor:
                if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == '.':

                    # If this empty cell is an exit, return distance + 1.
                    if next_row == 0 or next_row == rows - 1 or next_col == 0 or next_col == cols - 1:
                        return curr_distance + 1

                    # Otherwise, add this cell to 'queue' and mark it as visited.
                    maze[next_row][next_col] = '+'
                    queue.append([next_row, next_col, curr_distance + 1])

        return -1


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
    maze_5 = [["."]]
    entrance_5 = [0,0]
    expected_output_5 = -1



    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    solution_5 = Solution()
    test_1 = solution_1.nearestExit(maze_1, entrance_1)
    test_2 = solution_2.nearestExit(maze_2, entrance_2)
    test_3 = solution_3.nearestExit(maze_3, entrance_3)
    test_4 = solution_4.nearestExit(maze_4, entrance_4)
    test_5 = solution_5.nearestExit(maze_5, entrance_5)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
    print(f"\nTest 4 Output: {test_4} \nExpected Output: {expected_output_4}")
    print(f"\nTest 5 Output: {test_5} \nExpected Output: {expected_output_5}")


