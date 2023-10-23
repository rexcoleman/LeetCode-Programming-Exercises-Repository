from typing import List


class Solution:
    def setZeros(self, matrix: List[List[int]]) -> None:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        rows, cols = set(), set()

        # Essentially, we mark the rows and columns that are to be made zero
        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Iterate over the array once again and using the rows and cols sets, update the elements
        for i in range(num_rows):
            for j in range(num_cols):
                if i in rows or j in cols:
                    matrix[i][j] = 0



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

