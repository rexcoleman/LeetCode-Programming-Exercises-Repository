from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, columns = len(matrix), len(matrix[0])
        up = left = 0
        right = columns - 1
        down = rows - 1

        while len(result) < rows * columns:
            # Traverse from left to right
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Traverse downward
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Make sure we are now in a different row
            if up != down:
                # Traverse from right to left
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Make sure we are in a different column
            if left != right:
                # Traverwe upward
                for row in range(down -1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

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
