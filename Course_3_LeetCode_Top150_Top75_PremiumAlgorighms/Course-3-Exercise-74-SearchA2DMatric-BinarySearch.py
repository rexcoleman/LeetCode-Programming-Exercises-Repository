from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        # binary search
        left, right = 0, m * n - 1
        while left <= right:
            pivot_index = (left + right) // 2
            pivot_element = matrix[pivot_index // n][pivot_index % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_index - 1
                else:
                    left = pivot_index + 1

        return False




if __name__ == '__main__':

    # Inputs and Expected Outputs
    matrix_1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target_1 = 3
    expected_output_1 = True
    matrix_2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target_2 = 13
    expected_output_2 = False

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.searchMatrix(matrix_1, target_1)
    test_2 = solution_2.searchMatrix(matrix_2, target_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")