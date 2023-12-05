from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 3 * sum set => 3 of each value
        # Subtracting sum nums removes everything except
        # 2 * the value with only one element of it's value
        # Dividing by two isolates the value
        a = 3 * sum(set(nums))
        b = sum(nums)

        return (3 * sum(set(nums)) - sum(nums)) // 2


if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [2, 2, 3, 2]
    expected_output_1 = 3
    nums_2 = [0, 1, 0, 1, 0, 1, 99, 100, 100, 100]
    expected_output_2 = 99

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.singleNumber(nums_1)
    test_2 = solution_2.singleNumber(nums_2)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")