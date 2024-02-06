from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr.sort()
        count = 0
        run_length = 1
        for i in range(len(arr)):
            if arr[i-1] != arr[i]:
                if arr[i-1] + 1 == arr[i]:
                    count += run_length
                run_length = 0
            run_length += 1
        return count


if __name__ == '__main__':

    # Inputs and Expected Outputs
    arr_1 = [1, 2, 3]
    expected_output_1 = 2
    arr_2 = [1, 1, 3, 3, 5, 5, 7, 7]
    expected_output_2 = 0
    arr_3 = [1,1,2,2]
    expected_output_3 = 2

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.countElements(arr_1)
    test_2 = solution_2.countElements(arr_2)
    test_3 = solution_3.countElements(arr_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")


