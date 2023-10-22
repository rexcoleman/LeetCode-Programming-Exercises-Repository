from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        VISITED = 101
        rows, columns = len(matrix), len(matrix[0])
        # Four directions that we will move: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initialize direction: moving right
        current_direction = 0
        # Number of times we change direction
        change_direction = 0
        # Current place that we are at i (row, col)
        # Row is the row index.  Col is the colunn index
        row = col = 0
        # Store the first element and mark it as visited
        result = [matrix[0][0]]
        matrix[0][0] = VISITED

        while change_direction < 2:
            while True:
                # Calculate the next place that we will move to
                next_row = row + directions[current_direction][0]
                next_col = col + directions[current_direction][1]

                # Break if the next step is out of bounds
                if not (0 <= next_row < rows and 0 <= next_col < columns):
                    break
                # Break if the next step is on a visited cell
                if matrix[next_row][next_col] == VISITED:
                    break
                # Reset change_direction to zero since we did not break
                change_direction = 0
                # Update the current position to the next step
                row, col = next_row, next_col
                result.append(matrix[row][col])
                matrix[row][col] = VISITED

            # Change direction
            current_direction = (current_direction + 1) % 4
            # Increment change direction because we changed direction
            change_direction += 1

        return result


if __name__ == '__main__':

    # Inputs
    matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.spiralOrder(matrix_1)
    test_2 = solution_2.spiralOrder(matrix_2)

    print(f"Test 1: {test_1}")
    print('Expected Output 1: "[1, 2, 3, 6, 9, 8, 7, 4, 5]"')
    print(f"Test 2: {test_2}")
    print('Expected Output 2: "[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]"')
