from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        # Number of Senator
        n = len(senate)

        # Queues with Senator's Index.
        # Index will be used to find the next turn of Senator
        r_queue = deque()
        d_queue = deque()

        # Populate the Queues
        for i, s in enumerate(senate):
            if s == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)

        # While both parties have at least one Senator
        while r_queue and d_queue:
            # Pop the Next-Turn Senate from both Q.
            r_turn = r_queue.popleft()
            d_turn  = d_queue.popleft()

            # ONE having a larger index will be banned by a lower index
            # Lower index will again get Turn, so EN-Queue again
            # But ensure its turn comes in the next round only
            if d_turn < r_turn:
                d_queue.append(d_turn + n)
            else:
                r_queue.append(r_turn + n)

        # One's which Empty is not the winner
        return 'Radiant' if r_queue else 'Dire'

if __name__ == '__main__':

    # Inputs and Expected Outputs
    senate_1 = "RD"
    expected_output_1 = "Radiant"
    senate_2 = "RDDRRR"
    expected_output_2 = "Radiant"

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.predictPartyVictory(senate_1)
    test_2 = solution_2.predictPartyVictory(senate_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")