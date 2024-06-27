from typing import List
from itertools import product


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        self.ROWS = len(board)
        self.COLS = len(board[0])

        # Step 1). retrieve all border cells
        borders = (list(product(range(self.ROWS), [0, self.COLS - 1]))
                   + list(product([0, self.ROWS - 1], range(self.COLS))))
        # borders = (list(product([0, self.COLS - 1], range(self.ROWS)))
        #            + list(product([0, self.ROWS - 1], range(self.COLS))))

        # Step 2). mark the "escaped" cells, with any placeholder, e.g. 'E'
        for row, col in borders:
            self.DFS(board, row, col)

        # Step 3). flip the captured cells ('O'->'X') and the escaped one ('E'->'O')
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'E':
                    board[r][c] = 'O'

    def DFS(self, board, row, col):
        if row < 0 or row >= self.ROWS or col < 0 or col >= self.COLS:
            return
        if board[row][col] != 'O':
            return
        board[row][col] = 'E'
        # jump to the neighbors without boundary checks
        for ro, co in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            self.DFS(board, row + ro, col + co)


if __name__ == '__main__':

    # Inputs and Expected Outputs
    board_1 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    expected_output_1 = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]
    ]

    board_2 = [["X"]]
    expected_output_2 = [
        ["X"]
    ]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.solve(board_1)
    test_2 = solution_2.solve(board_2)

    # Print Results
    print(f"\nResult 1: {board_1} \nExpected Result: {expected_output_1}")
    print(f"\nResult 1: {board_2} \nExpected Result: {expected_output_2}")