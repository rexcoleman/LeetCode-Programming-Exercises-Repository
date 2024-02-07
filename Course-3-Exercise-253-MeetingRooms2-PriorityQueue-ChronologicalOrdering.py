import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        len_intervals = len(intervals)
        if len_intervals < 2:
            return len_intervals

        used_rooms = 0

        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])

        start_pointer, end_pointer = 0, 0

        while start_pointer < len_intervals:
            if start_times[start_pointer] >= end_times[end_pointer]:
                used_rooms -= 1
                end_pointer += 1

            used_rooms += 1
            start_pointer += 1

        return used_rooms


if __name__ == '__main__':

    # Inputs and Expected Outputs
    intervals_1 = [[0, 30], [5, 10], [15, 20]]
    expected_output_1 = 2
    intervals_2 = [[7, 10], [2, 4]]
    expected_output_2 = 1

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.minMeetingRooms(intervals_1)
    test_2 = solution_2.minMeetingRooms(intervals_2)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")