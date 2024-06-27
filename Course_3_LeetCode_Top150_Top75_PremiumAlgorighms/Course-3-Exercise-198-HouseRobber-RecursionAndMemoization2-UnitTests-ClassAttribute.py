import unittest
from typing import List

class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.robFrom(0, nums)

    def robFrom(self, i, nums):
        if i >= len(nums):
            return 0
        if i in self.memo:
            return self.memo[i]
        ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])
        self.memo[i] = ans
        return ans

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rob_empty(self):
        self.assertEqual(self.solution.rob([]), 0)

    def test_rob_single(self):
        self.assertEqual(self.solution.rob([1]), 1)

    def test_rob_example1(self):
        self.assertEqual(self.solution.rob([1,2,3,1]), 4)

    def test_rob_example2(self):
        self.assertEqual(self.solution.rob([2,7,9,3,1]), 12)

    def test_rob_large(self):
        self.assertEqual(self.solution.rob([2,1,1,2]), 4)

if __name__ == '__main__':
    unittest.main()
