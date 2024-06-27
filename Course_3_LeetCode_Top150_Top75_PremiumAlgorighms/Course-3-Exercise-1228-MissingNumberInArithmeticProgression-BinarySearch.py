from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        step = (arr[-1] - arr[0]) // len(arr)

        while left <= right:
            mid = (left + right) // 2
            # Check if the difference between the mid element and the first element
            # is equal to mid times the step. If not, missing number is in left half.
            if arr[mid] != arr[0] + mid * step:
                right = mid - 1
            else:
                left = mid + 1

        # After finding the point where the pattern breaks, calculate the missing number.
        return arr[0] + step * left



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

