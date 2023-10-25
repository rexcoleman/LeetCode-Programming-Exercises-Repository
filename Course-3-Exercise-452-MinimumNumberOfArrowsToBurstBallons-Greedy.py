from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort by x_end
        points.sort(key = lambda x: x[1])

        arrows = 1
        first_end = points[0][1]
        for x_start, x_end in points:
            # if the current balloon starts after the end of another one,
            # one needs one more arrow
            if first_end < x_start:
                arrows += 1
                first_end = x_end
        return arrows


if __name__ == '__main__':

    # Inputs
    points_1 = [[10, 16], [2, 8], [1, 6], [7, 12]]
    points_2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    points_3 = [[1, 2], [2, 3], [3, 4], [4, 5]]

    # Run tests

    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()

    test_1 = solution_1.findMinArrowShots(points_1)
    test_2 = solution_2.findMinArrowShots(points_2)
    test_3 = solution_3.findMinArrowShots(points_3)

    print(f"Test 1: {test_1}")
    print("Expected Output 1: 2")
    print(f"Test 2: {test_2}")
    print("Expected Output 2: 4")
    print(f"Test 3: {test_3}")
    print("Expected Output 2: 2")