from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        curr_gain = 0
        answer = 0

        for i in range(len(gas)):
            # gain[i] = gas[i] - cost[i]
            total_gain += gas[i] - cost[i]
            curr_gain += gas[i] - cost[i]

            # If we meet a 'valley,' start over from the next station
            # with zero initial gas.
            if curr_gain < 0:
                curr_gain = 0
                answer = i + 1

        return answer if total_gain >= 0 else -1




if __name__ == '__main__':

    # Inputs
    gas1 = [1, 2, 3, 4, 5]
    cost1 = [3, 4, 5, 1, 2]
    gas2 = [2, 3, 4]
    cost2 = [3, 4, 3]

    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.canCompleteCircuit(gas1, cost1)
    test_2 = solution_2.canCompleteCircuit(gas2, cost2)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")