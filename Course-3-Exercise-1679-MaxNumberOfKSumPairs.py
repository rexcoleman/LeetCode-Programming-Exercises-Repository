from collections import defaultdict
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums_map = defaultdict(int)
        ans = 0

        for i in range(len(nums)):
            target = k - nums[i]
            if target in nums_map and nums_map[target] > 0:
                nums_map[target] -= 1
                ans += 1
            else:
                nums_map[nums[i]] += 1
        return ans


if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [1, 2, 3, 4]
    k_1 = 5
    expected_output_1 = 2
    nums_2 = [3, 1, 3, 4, 3]
    k_2 = 6
    expected_output_2 = 1

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.maxOperations(nums_1, k_1)
    test_2 = solution_2.maxOperations(nums_2, k_2)

    # Prnt Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 1 Output: {test_2} \nExpected Output: {expected_output_2}")
