from collections import defaultdict
from typing import List


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        val_map = defaultdict(int)
        sce = float('inf')

        # for i in range(len(mat)):
        #     for j in range(len(mat[i])):
        #         val_map[mat[i][j]] += 1

        for row in mat:
            for num in row:
                val_map[num] += 1

        for key, val in val_map.items():
            if val == len(mat):
                sce = min(sce, key)

        return sce if sce != float('inf') else -1


if __name__ == '__main__':
    # Inputs and Expected Outputs
    mat_1 = [[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]
    expected_output_1 = 5
    mat_2 = [[1, 2, 3], [2, 3, 4], [2, 3, 5]]
    expected_output_2 = 2

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.smallestCommonElement(mat_1)
    test_2 = solution_2.smallestCommonElement(mat_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")