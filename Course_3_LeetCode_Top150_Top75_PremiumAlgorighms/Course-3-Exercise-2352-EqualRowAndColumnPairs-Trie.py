from collections import defaultdict, Counter
from typing import List

class TreeNode:
    def __init__(self):
        self.count = 0
        self.children = {}

    def __str__(self, level=0):
        ret = "  " * level + f"Count: {self.count}\n"
        for key, child in self.children.items():
            ret += "  " * level + f"Key: {key}\n" + child.__str__(level + 1)
        return ret

class Trie:
    def __init__(self):
        self.trie = TreeNode()

    def __str__(self):
        return self.trie.__str__()

    def insert(self, array):
        my_trie = self.trie
        for a in array:
            if a not in my_trie.children:
                my_trie.children[a] =  TreeNode()
            my_trie = my_trie.children[a]
        my_trie.count += 1

    def search(self, array):
        my_trie = self.trie
        for a in array:
            if a in my_trie.children:
                my_trie = my_trie.children[a]
            else:
                return 0
        return my_trie.count

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        my_trie = Trie()
        count = 0
        n = len(grid)

        for row in grid:
            my_trie.insert(row)

        for c in range(n):
            col_array = [grid[i][c] for i in range(n)]
            count += my_trie.search(col_array)

        return count


if __name__ == '__main__':

    # Inputs and Expected Outputs:
    grid_1 = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    expected_output_1 = 1
    grid_2 = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    expected_output_2 = 3

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.equalPairs(grid_1)
    test_2 = solution_2.equalPairs(grid_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
