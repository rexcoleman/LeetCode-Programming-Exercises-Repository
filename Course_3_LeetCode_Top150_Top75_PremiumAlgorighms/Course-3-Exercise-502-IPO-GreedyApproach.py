from heapq import heappush, heappop
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()
        # heapq is a min heap, but we need a max heap
        # so we will store negated elements
        q = []
        ptr = 0
        for i in range(k):
            while ptr < n and projects[ptr][0] <= w:
                # push a negated element
                heappush(q, -projects[ptr][1])
                ptr += 1
            if not q:
                break
            # pop a negated element
            w += -heappop(q)
        return w


if __name__ == '__main__':

    # Inputs and Expected Outputs
    k_1 = 2
    w_1 = 0
    profits_1 = [1, 2, 3]
    capital_1 = [0, 1, 1]
    expected_output_1 = 4
    k_2 = 3
    w_2 = 0
    profits_2 = [1, 2, 3]
    capital_2 = [0, 1, 2]
    expected_output_2 = 6

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.findMaximizedCapital(k_1, w_1, profits_1, capital_1)
    test_2 = solution_2.findMaximizedCapital(k_2, w_2, profits_2, capital_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")

