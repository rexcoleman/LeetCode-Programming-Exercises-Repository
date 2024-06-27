from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        answer, k = 0, -float('inf')

        for x, y in intervals:
            if x >= k:
                k = y
            else:
                answer += 1
        return answer


if __name__ == '__main__':

    # Inputs and Expected Outputs
    intervals_1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
    expected_output_1 = 1
    intervals_2 = [[1, 2], [1, 2], [1, 2]]
    expected_output_2 = 2
    intervals_3 = [[1, 2], [2, 3]]
    expected_output_3 = 0
    intervals_4 = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
    expected_output_4 = 7

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    test_1 = solution_1.eraseOverlapIntervals(intervals_1)
    test_2 = solution_2.eraseOverlapIntervals(intervals_2)
    test_3 = solution_3.eraseOverlapIntervals(intervals_3)
    test_4 = solution_4.eraseOverlapIntervals(intervals_4)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
    print(f"\nTest 4 Output: {test_4} \nExpected Output: {expected_output_4}")