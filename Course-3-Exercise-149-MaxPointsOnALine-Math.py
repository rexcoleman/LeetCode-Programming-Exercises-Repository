from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        pass


if __name__ == '__main__':

    # Inputs and Expected Outputs
    points_1 = [[1, 1], [2, 2], [3, 3]]
    expected_output_1 = 3
    points_2 = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    expected_output_2 = 4

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.maxPoints(points_1)
    test_2 = solution_2.maxPoints(points_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")

