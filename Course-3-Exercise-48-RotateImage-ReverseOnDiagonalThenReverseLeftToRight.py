from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j -1] = matrix[i][-j -1], matrix[i][j]



if __name__ == '__main__':

    # Inputs

    matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]



                                                                                                                                                                                                                                                                                                                                                                                                   # Run Tests

    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.rotate(matrix_1)
    test_2 = solution_2.rotate(matrix_2)

    print(f"Test 1: {matrix_1}")
    print("Expected Output 1: [[7,4,1],[8,5,2],[9,6,3]]")
    print(f"Test 2: {matrix_2}")
    print("Expected Output 2: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]")


