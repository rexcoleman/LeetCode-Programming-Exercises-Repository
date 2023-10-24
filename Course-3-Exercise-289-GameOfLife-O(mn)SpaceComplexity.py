from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # Neighbors array to find 8 neighboring cells for a given cell
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        rows = len(board)
        cols = len(board[0])

        # Create a copy of the original board
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        # Iterate through board cell by cell.
        for row in range(rows):
            for col in range(cols):
                # For each cell count the number of live neighbors.
                live_neighbors = 0
                for neighbor in neighbors:
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # Check the validity of the neighboring cell and if it was originally a live cell.
                    # The evaluation is done against the copy, since that is never updated.
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (copy_board[r][c] == 1):
                        live_neighbors += 1

                # Rule 1 or Rule 3
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                # Rule 4
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1



if __name__ == '__main__':

    # Inputs
    board_1 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    board_2 = [[1,1],[1,0]]

    # Run tests
    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.gameOfLife(board_1)
    test_2 = solution_2.gameOfLife(board_2)

    print(f"Test 1: {board_1}")
    print("Expected Output 1: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]")
    print(f"Test 2: {board_2}")
    print("Expected Output 2: [[1,1],[1,1]]")