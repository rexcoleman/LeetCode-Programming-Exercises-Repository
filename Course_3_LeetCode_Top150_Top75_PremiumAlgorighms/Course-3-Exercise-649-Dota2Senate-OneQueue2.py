from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        # Eligible Senators of each party
        r_count = senate.count('R')
        d_count = len(senate) - r_count

        # Floating Ban Count
        d_floating_ban = 0
        r_floating_ban = 0

        # Queue of Senators
        queue = deque(senate)

        # While any party has eligible Senators
        while r_count and d_count:

            # Pop the senator with turn
            curr = queue.popleft()

            # If eligible, float the ban on the other party, enqueue again.
            # If not, decrement the floating ban and count of the party.
            if curr == 'D':
                if d_floating_ban:
                    d_floating_ban -= 1
                    d_count -= 1
                else:
                    r_floating_ban += 1
                    queue.append('D')
            else:
                if r_floating_ban:
                    r_floating_ban -= 1
                    r_count -= 1
                else:
                    d_floating_ban += 1
                    queue.append('R')

        # Return the party with eligible Senators
        return 'Radiant' if r_count else 'Dire'


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