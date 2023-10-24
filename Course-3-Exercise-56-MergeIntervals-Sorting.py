import collections
from typing import List
from collections import defaultdict

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged




if __name__ == '__main__':

    #Inputs
    intervals_1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals_2 = [[1, 4], [4, 5]]

    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.merge(intervals_1)
    test_2 = solution_2.merge(intervals_2)

    print(f"Test 1: {test_1}")
    print("Expected Output 1: [[1,6],[8,10],[15,18]]")
    print(f"Test 2: {test_2}")
    print("Expected Output 2: [[1,5]]")