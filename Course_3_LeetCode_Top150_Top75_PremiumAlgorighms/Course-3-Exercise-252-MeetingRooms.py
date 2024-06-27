from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True


if __name__ == '__main__':

    # Inputs and Expected Outputs
    intervals_1 = [[0, 30], [5, 10], [15, 20]]
    expected_output_1 = False
    intervals_2 = [[7, 10], [2, 4]]
    expected_output_2 = True

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.canAttendMeetings(intervals_1)
    test_2 = solution_2.canAttendMeetings(intervals_2)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
