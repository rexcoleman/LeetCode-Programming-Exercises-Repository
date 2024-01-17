from collections import defaultdict, deque
from typing import List


class UnionFind:
    def __init__(self, n):
        self.u = list(range(n))

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.u[ra] = rb

    def find(self, a):
        while self.u[a] != a:
            a = self.u[a]
        b = list(self.u)
        return a


class Solution:
    def findCircleNum(self, isConnected: [List[List[int]]]) -> int:
        if not isConnected:
            return 0
        s = len(isConnected)

        uf = UnionFind(s)
        for r in range(s):
            for c in range(r,s):
                if isConnected[r][c] == 1:
                    uf.union(r,c)

        g = [uf.find(i) for i in range(s)]
        print(g)
        return len(set([uf.find(i) for i in range(s)]))

if __name__ == '__main__':

    # Inputs and Expected Outputs
    isConnected_1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    expected_output_1 = 2
    isConnected_2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    expected_output_2 = 3
    isConnected_3 = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    expected_output_3 = 1

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.findCircleNum(isConnected_1)
    test_2 = solution_2.findCircleNum(isConnected_2)
    test_3 = solution_3.findCircleNum(isConnected_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
