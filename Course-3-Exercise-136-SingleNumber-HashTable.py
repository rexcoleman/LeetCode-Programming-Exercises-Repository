from typing import List
from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        for i in hash_table:
            if hash_table[i] == 1:
                return i
            




if __name__ == '__main__':

    # Inputs
    nums1 = [2, 2, 1]
    nums2 = [4, 1, 2, 1, 2]
    nums3 = [1]

    solution1 = Solution()
    solution2 = Solution()
    solution3 = Solution()

    test_1 = solution1.singleNumber(nums1)
    test_2 = solution2.singleNumber(nums2)
    test_3 = solution3.singleNumber(nums3)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")
    print(f"Test 3: {test_3}")