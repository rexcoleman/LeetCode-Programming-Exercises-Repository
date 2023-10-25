import bisect
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = bisect.bisect_left(intervals, newInterval)
        result = intervals[:i]
        a = [newInterval] + intervals[i:]
        print(a)
        for interval in [newInterval] + intervals[i:]:
            if result and result[-1][1] >= interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result


if __name__ == '__main__':
    # Inputs
    intervals_1 = [[1,3],[6,9]]
    new_interval_1 = [2, 5]
    intervals_2 = [[1,2],[4,5],[6,7],[8,10],[12,16]]
    new_interval_2 = [4,8]


    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.insert(intervals_1, new_interval_1)
    test_2 = solution_2.insert(intervals_2, new_interval_2)

    print(f"Test 1: {test_1}")
    print("Expected Output 1: [[1,5],[6,9]]")
    print(f"Test 2: {test_2}")
    print("Expected Output 2: [[1,2],[3,10],[12,16]]")