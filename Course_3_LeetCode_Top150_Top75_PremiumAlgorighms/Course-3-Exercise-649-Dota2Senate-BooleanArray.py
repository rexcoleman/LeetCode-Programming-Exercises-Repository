from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        # Number of Senators
        N = len(senate)

        # To mark Banned Senators
        banned = [False] * N

        # Count of Each Type of Senator who are not-banned
        r_count = senate.count('R')
        d_count = N - r_count

        # Ban the candidate "to_ban", immediate next to "start_at"
        def ban(to_ban, start_at):
            # Find the next eligible senator of "to_ban" type
            # On found, mark him as banned
            pointer = start_at
            while True:
                if senate[pointer] == to_ban and not banned[pointer]:
                    banned[pointer] = True
                    break
                pointer = (pointer + 1) % N

        # Turn of Senator at this Index
        turn = 0

        # While both parties have at least one senator
        while r_count > 0 and d_count > 0:
            if not banned[turn]:
                if senate[turn] == 'R':
                    ban('D', (turn + 1) % N)
                    d_count -= 1
                else:
                    ban('R', (turn + 1) % N)
                    r_count -= 1
            turn = (turn + 1) % N

        return 'Radiant' if d_count == 0 else 'Dire'


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