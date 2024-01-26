from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Start at an eating speed of 1.
        speed = 1
        while True:
            # hour_spent stands for the total hour Koko spends with
            # the given eating speed.
            hour_spent = 0

            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / speed)
            for pile in piles:
                hour_spent += ceil(pile / speed)

            # Check if Koko can finish all the piles within h hours,
            # If so, return speed. Otherwise, let speed increment by
            # 1 and repeat the previous iteration.
            if hour_spent <= h:
                return speed
            else:
                speed += 1


if __name__ == '__main__':

    # Inputs and Expected Outputs
    piles_1 = [3, 6, 7, 11]
    h_1 = 8
    expected_output_1 = 4
    piles_2 = [30, 11, 23, 4, 20]
    h_2 = 5
    expected_output_2 = 30
    piles_3 = [30, 11, 23, 4, 20]
    h_3 = 6
    expected_output_3 = 23

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.minEatingSpeed(piles_1, h_1)
    test_2 = solution_2.minEatingSpeed(piles_2, h_2)
    test_3 = solution_3.minEatingSpeed(piles_3, h_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")