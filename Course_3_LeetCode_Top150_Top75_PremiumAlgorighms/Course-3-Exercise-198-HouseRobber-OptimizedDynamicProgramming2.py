from typing import List


class Solution:


    def rob(self, nums: List[int]) -> int:

        len_nums = len(nums)
        # Special handling for empty case.
        if not nums:
            return 0
        robNext, robNextPlusOne = nums[len_nums - 1], 0
        currMax = 0

        # DP table calculations.
        for i in range(len_nums - 2, -1, -1 ):
            currMax = max(robNext, robNextPlusOne + nums[i])
            robNext, robNextPlusOne = currMax, robNext

        return robNext


if __name__ == '__main__':
    # Inputs and Expected Outputs
    nums_1 = [1,2,3,1]
    expected_output_1 = 4
    nums_2 = [2,7,9,3,1]
    expected_output_2 = 12
    nums_3 = [1]
    expected_output_3 = 1


    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.rob(nums_1)
    test_2 = solution_2.rob(nums_2)
    test_3 = solution_3.rob(nums_3)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3 Result: {test_3} \nExpected Result: {expected_output_3}")
