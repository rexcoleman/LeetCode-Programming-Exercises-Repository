from typing import List


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        answer = [ [0] * len(mat1[0]) for row in mat1]
        a = 2



if __name__ == '__main__':

    # Inuts and Expected Outputs
    mat1_1 = [[1, 0, 0], [-1, 0, 3]]
    mat2_1 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
    expected_output_1 = [[7, 0, 0], [-7, 0, 3]]
    mat1_2 = [[0]]
    mat2_2 = [[0]]
    expected_output_2 = [[0]]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.multiply(mat1_1, mat2_1)
    test_2 = solution_2.multiply(mat1_2, mat2_2)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")