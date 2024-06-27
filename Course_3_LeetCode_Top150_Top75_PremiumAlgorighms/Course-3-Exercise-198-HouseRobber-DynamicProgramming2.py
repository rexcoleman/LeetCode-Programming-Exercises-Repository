from typing import List


class Solution:


    def rob(self, nums: List[int]) -> int:

        len_nums = len(nums)
        # Special handling for empty case.
        if not nums:
            return 0
        maxRobbedAmount = [None for _ in range(len_nums + 1)]

        # Base case initialization.
        maxRobbedAmount[len_nums], maxRobbedAmount[len_nums - 1] = 0, nums[len_nums - 1]

        # DP table calculations.
        for i in range(len_nums - 2, -1, -1 ):
            maxRobbedAmount[i] = max(maxRobbedAmount[i+1], maxRobbedAmount[i+2] + nums[i])

        return maxRobbedAmount[0]


if __name__ == '__main__':
    # Inputs and Expected Outputs
    nums_1 = [1,2,3,1]
    expected_output_1 = 4
    nums_2 = [2,7,9,3,1]
    expected_output_2 = 12


    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.rob(nums_1)
    test_2 = solution_2.rob(nums_2)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
