from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        len_arr = len(arr)
        if len_arr == 3:
            return True
        occurrences = defaultdict(int)
        for num in arr:
            occurrences[num] += 1
        values = list(occurrences.values())
        set_1 = set(values)
        return len(set_1) == len(values)


if __name__ == '__main__':

    # Inputs and Expected Outputs
    arr_1 = [1, 2, 2, 1, 1, 3]
    expected_output_1 = True
    arr_2 = [1, 2]
    expected_output_2 = False
    arr_3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    expected_output_3 = True

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.uniqueOccurrences(arr_1)
    test_2 = solution_2.uniqueOccurrences(arr_2)
    test_3 = solution_3.uniqueOccurrences(arr_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")