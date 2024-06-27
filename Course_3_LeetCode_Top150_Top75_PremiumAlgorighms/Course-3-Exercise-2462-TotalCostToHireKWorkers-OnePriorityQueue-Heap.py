import heapq
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # Add the first k workers with section id of 0 and
        # the last k workers with section id of 1 (without duplication) to pq.
        pq = []
        for i in range(candidates):
            pq.append((costs[i], 0))
        for i in range(max(candidates, len(costs) - candidates), len(costs)):
            pq.append((costs[i], 1))

        heapify(pq)
        answer = 0
        next_head, next_tail = candidates, len(costs) - candidates - 1

        # Only refill pq if there are workers outside.
        for _ in range(k):
            curr_cost, curr_section_id = heappop(pq)
            answer += curr_cost
            if next_head <= next_tail:
                if curr_section_id == 0:
                    heappush(pq, (costs[next_head], 0))
                    next_head += 1
                else:
                    heappush(pq, (costs[next_tail], 1))
                    next_tail -= 1
        return answer


if __name__ == '__main__':

    # Inputs and Expected Outputs
    costs_1 = [17, 12, 10, 2, 7, 2, 11, 20, 8]
    k_1 = 3
    candidates_1 = 4
    expected_outcome_1 = 11
    costs_2 = [1, 2, 4, 1]
    k_2 = 3
    candidates_2 = 3
    expected_outcome_2 = 4

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.totalCost(costs_1, k_1, candidates_1)
    test_2 = solution_2.totalCost(costs_2, k_2, candidates_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_outcome_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_outcome_2}")