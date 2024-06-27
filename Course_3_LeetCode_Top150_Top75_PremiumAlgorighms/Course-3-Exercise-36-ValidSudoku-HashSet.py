from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        # Use hash sets to record the status
        rows = [set() for _ in range(N)]
        columns = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # Check if position is filled with a number
                if val == '.':
                    continue

                # Check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check the column
                if val in columns[c]:
                    return False
                columns[c].add(val)

                # Check the box
                box_index = (r // 3) * 3 + (c // 3)
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)
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