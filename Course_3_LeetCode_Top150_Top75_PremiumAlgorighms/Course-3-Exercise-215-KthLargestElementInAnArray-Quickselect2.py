import heapq
import random
from typing import List


class Solution:


    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)

            if k <= len(left):
                return quickSelect(left, k)
            if len(left) + len(mid) < k:
                return quickSelect(right, k - len(left) - len(mid))

            return pivot
        return quickSelect(nums, k)


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