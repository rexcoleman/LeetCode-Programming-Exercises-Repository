import heapq
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # head_workers stores the first k workers.
        # tail_workers stores at most last k workers without any workers from the first k workers.
        head_workers = costs[:candidates]
        tail_workers = costs[max(candidates, len(costs) - candidates):]
        heapify(head_workers)
        heapify(tail_workers)

        answer = 0
        next_head, next_tail = candidates, len(costs) - candidates - 1

        for _ in range(k):
            if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]:
                answer += heappop(head_workers)

                # Only refill the queue if there are workers outside the two queues.
                if next_head <= next_tail:
                    heappush(head_workers, costs[next_head])
                    next_head += 1
            else:
                answer += heappop(tail_workers)
                # Only refill the queue if there are workers outside the two queues.
                if next_head <= next_tail:
                    heappush(tail_workers, costs[next_tail])
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