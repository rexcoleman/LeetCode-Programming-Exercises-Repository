from typing import List

class Solution:
    def setZeros(self, matrix: List[List[int]]) -> None:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        for i in range(num_rows):
            for j in range(1, num_cols):
                # If an element is zero, we set the first element of the corresponding row and column to 0?
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, num_rows):
            for j in range(1, num_cols):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(1, num_cols):
                matrix[0][j] = 0
            for i in range(1, num_rows):
                matrix[i][0] = 0


if __name__ == '__main__':

    # Inputs
    matrix_1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    matrix_2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

    # Run tests

    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.setZeros(matrix_1)
    test_2 = solution_2.setZeros(matrix_2)

    print(f"Test 1: {matrix_1}")
    print("Expected Output 1: [[1,0,1],[0,0,0],[1,0,1]]")
    print(f"Test 2: {matrix_2}")
    print("Expected Output 2: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]")

