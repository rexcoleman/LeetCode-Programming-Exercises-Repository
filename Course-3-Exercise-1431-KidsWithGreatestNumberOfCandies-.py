from typing import List
from heapq import heappush, heapify, heappop


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        min_required_candies = max(candies) - extraCandies
        for candy in candies:
            output.append(candy >= min_required_candies)
        return output


if __name__ == '__main__':

    # Inputs and Expected Outputs
    candies_1 = [2, 3, 5, 1, 3]
    extraCandies_1 = 3
    expected_output_1 = [True, True, True, False, True]
    candies_2 = [4, 2, 1, 1, 2]
    extraCandies_2 = 1
    expected_output_2 = [True, False, False, False, False]
    candies_3 = [12, 1, 12]
    extraCandies_3 =    10
    expected_output_3 = [True, False, True]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.kidsWithCandies(candies_1, extraCandies_1)
    test_2 = solution_2.kidsWithCandies(candies_2, extraCandies_2)
    test_3 = solution_3.kidsWithCandies(candies_3, extraCandies_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
