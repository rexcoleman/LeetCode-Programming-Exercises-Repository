from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        len_arr = len(arr)
        pattern_dist = abs((arr[-1] - arr[0])/len_arr)
        if pattern_dist == 0:
            return arr[0]
        for i in range(1, len_arr):
            if abs(arr[i] - arr[i-1]) > pattern_dist:
                return int((arr[i] + arr[i-1])/2)


if __name__ == '__main__':

    # Inputs and Expected Outputs
    arr_1 = [5, 7, 11, 13]
    expected_output_1 = 9
    arr_2 = [15, 13, 12]
    expected_output_2 = 14

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.missingNumber(arr_1)
    test_2 = solution_2.missingNumber(arr_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")