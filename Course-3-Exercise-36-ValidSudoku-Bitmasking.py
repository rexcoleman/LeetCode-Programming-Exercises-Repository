from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        # Use binary number to check for previous occurrence
        rows = [0] * N
        columns = [0] * N
        boxes = [0] * N

        for r in range(N):
            for c in range(N):
                # Check if the position is filled with a number
                if board[r][c] == ".":
                    continue

                position = int(board[r][c]) - 1

                # Check the row
                if rows[r] & (1 << position):
                    return False
                rows[r] |= (1 << position)

                # Check the column
                if columns[c] & (1 << position):
                    return False
                columns[c] |= (1 << position)

                # Check the box
                box_index = (r // 3) * 3 + (c // 3)
                if boxes[box_index] & (1 << position):
                    return False
                boxes[box_index] |= (1 << position)

        return True


if __name__ == '__main__':

    # Inputs
    board_1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    board_2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    # Run tests

    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.isValidSudoku(board_1)
    tess_2 = solution_2.isValidSudoku(board_2)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {tess_2}")

    print(f'Expected Output 1: "true"')
    print(f'Expected Output 2: "false"')