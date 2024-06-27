from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for interval in intervals:
            # the new interval is after the range of other interval,
            # so we can leave the current interval baecause
            # the new one does not overlap with it
            if interval[1] < newInterval[0]:
                result.append(interval)

            # the new interval's range is before the other,
            # so we can add the new interval and update it to the current one
            elif interval[0] > newInterval[1]:
                result.append(newInterval)

            # the new interval is in the range of the other interval,
            # we have an overlap, so we must choose the min for start and max for end of interval
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        result.append(newInterval)
        return result


if __name__ == '__main__':
    # Inputs
    intervals_1 = [[1,3],[6,9]]
    new_interval_1 = [2, 5]
    intervals_2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new_interval_2 = [4,8]


    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.insert(intervals_1, new_interval_1)
    test_2 = solution_2.insert(intervals_2, new_interval_2)

    print(f"Test 1: {test_1}")
    print("Expected Output 1: [[1,5],[6,9]]")
    print(f"Test 2: {test_2}")
    print("Expected Output 2: [[1,2],[3,10],[12,16]]")