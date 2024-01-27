from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Initalize the left and right boundaries
        left = 1
        right = max(piles)

        while left < right:
            # Get the middle index between left and right boundary indexes.
            # hour_spent stands for the total hour Koko spends.
            mid = (left + right) // 2
            hour_spent = 0

            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / middle)
            for pile in piles:
                hour_spent += ceil(pile / mid)

            # Check if middle is a workable speed, and cut the search space by half.
            # The equal sign is on this term because everything to the right is workable (inclusive)
            # If we do while left < right then we do right = mid.
            # If we do while left <= right then we do right = mid - 1.  If we do not include the mid - 1 part
            # Then we could get stuck in an endless loop where left == right
            # Note that thd toggle is on this term with the = sign
            # because everything to the right is workable (inclusive) and we want to do bisect.bisectleft
            if hour_spent <= h:
                right = mid
            else:
                left = mid + 1

        # Once the left and right boundaries coincide, we find the target value,
        # that is, the minimum workable eating speed.
        return left


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