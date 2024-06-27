import math
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalSum = 0
        currMaxSum = 0
        currMinSum = 0
        maxSum = -math.inf
        minSum = math.inf

        for num in nums:
            totalSum += num
            currMaxSum = max(currMaxSum + num, num)
            currMinSum = min(currMinSum + num, num)
            maxSum = max(maxSum, currMaxSum)
            minSum = min(minSum, currMinSum)

        return maxSum if maxSum < 0 else max(maxSum, totalSum - minSum)




if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [1, -2, 3, -2]
    expected_output_1 = 3
    nums_2 = [5, -3, 5]
    expected_output_2 = 10
    nums_3 = [-3, -2, -3]
    expected_output_3 = -2

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.maxSubarraySumCircular(nums_1)
    test_2 = solution_2.maxSubarraySumCircular(nums_2)
    test_3 = solution_3.maxSubarraySumCircular(nums_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")