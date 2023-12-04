import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_value = min(nums)
        max_value = max(nums)
        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1

        remain = k

        for num in range(len(count) -1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                # Note the + min_value factor.  This reverses the subtraction of min_value when we
                # iterated through nums to create the count array
                return num + min_value

        return -1








if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = nums = [3,2,1,5,6,4]
    k_1 = 2
    expected_output_1 = 5
    nums_2 = [3,2,3,1,2,4,5,5,6]
    k_2 = 4
    expected_output_2 = 4

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.findKthLargest(nums_1, k_1)
    test_2 = solution_2.findKthLargest(nums_2, k_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
