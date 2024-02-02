from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        answer = 0
        k, slow, fast = 0, 0, 1

        while fast < len(points):
            k = points[slow][1]
            while k >= points[fast][0]:
                fast += 1
                if fast >= len(points):
                    break
            answer += 1
            slow = fast
            fast += 1
        if slow < len(points):
            answer += len(points) - slow
        return answer

if __name__ == '__main__':

    # Inputs and Expected Outputs
    points_1 = [[10, 16], [2, 8], [1, 6], [7, 12]]
    expected_output_1 = 2
    points_2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    expected_output_2 = 4
    points_3 = [[1, 2], [2, 3], [3, 4], [4, 5]]
    expected_output_3 = 2

    # Run tests

    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.findMinArrowShots(points_1)
    test_2 = solution_2.findMinArrowShots(points_2)
    test_3 = solution_3.findMinArrowShots(points_3)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")