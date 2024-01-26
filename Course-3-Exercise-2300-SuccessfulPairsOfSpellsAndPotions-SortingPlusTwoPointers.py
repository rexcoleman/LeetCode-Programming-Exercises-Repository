import bisect
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        sorted_spells = [(spell, index) for index, spell in enumerate(spells)]
        sorted_spells.sort()
        potions.sort()

        answer = [0] * len(spells)
        m = len(potions)
        potion_index = m - 1

        for spell, index in sorted_spells:
            while potion_index >= 0 and (spell * potions[potion_index]) >= success:
                potion_index -= 1
            answer[index] = m - (potion_index + 1)

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