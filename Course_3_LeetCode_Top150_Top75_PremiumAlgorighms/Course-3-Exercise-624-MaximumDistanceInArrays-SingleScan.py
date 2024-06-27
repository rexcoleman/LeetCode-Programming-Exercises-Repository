from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_val = arrays[0][-1]
        min_val = arrays[0][0]
        max_distance = 0
        for i in range(1, len(arrays)):
            i_max = arrays[i][-1]
            i_min = arrays[i][0]
            max_distance = max(max_distance, i_max - min_val, max_val - i_min)
            max_val = max(max_val, i_max)
            min_val = min(min_val, i_min)

        return max_distance


if __name__ == '__main__':

    # Inputs and Expected Outputs
    arrays_1 = [[1, 2, 3], [4, 5], [1, 2, 3]]
    expected_output_1 = 4
    arrays_2 = [[1], [1]]
    expected_output_2 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.maxDistance(arrays_1)
    test_2 = solution_2.maxDistance(arrays_2)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")