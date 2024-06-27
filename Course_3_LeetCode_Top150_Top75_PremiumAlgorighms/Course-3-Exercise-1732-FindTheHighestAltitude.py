import math
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        curr_altitude = 0
        for i in range(len(gain)):
            curr_altitude += gain[i]
            highest_altitude = max(highest_altitude, curr_altitude)
        return highest_altitude



if __name__ == '__main__':

    # Inputs and Expected Outputs
    gain_1 = [-5, 1, 5, 0, -7]
    expected_output_1 = 1
    gain_2 = [-4, -3, -2, -1, 4, 3, 2]
    expected_output_2 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.largestAltitude(gain_1)
    test_2 = solution_2.largestAltitude(gain_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
