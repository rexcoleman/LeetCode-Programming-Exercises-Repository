import bisect
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        # Sort the potions array in increasing order.
        potions.sort()
        answer = []

        m = len(potions)
        maxPotion = potions[m - 1]

        for spell in spells:
            # Minimum value of potion whose product with current spell
            # will be at least success or more.
            minPotion = (success + spell - 1) // spell

            # Check if we don't have any potion which can be used.
            if minPotion > maxPotion:
                answer.append(0)
                continue

            # We can use the found potion, and all potion in its right
            # (as the right potions are greater than the found potion).

            left, right = 0, m - 1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] < minPotion:
                    left = mid + 1
                else:
                    right = mid - 1

            answer.append(m - left)

        return answer


if __name__ == '__main__':

    # Inputs and Expected Outputs
    spells_1 = [5, 1, 3]
    potions_1 = [1, 2, 3, 4, 5]
    success_1 = 7
    expected_output_1 = [4, 0, 3]
    spells_2 = [3, 1, 2]
    potions_2 = [8, 5, 8]
    success_2 = 16
    expected_output_2 = [2, 0, 2]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.successfulPairs(spells_1, potions_1, success_1)
    test_2 = solution_2.successfulPairs(spells_2, potions_2, success_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")