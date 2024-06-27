from typing import List


class UnionFind:
    def __init__(self, total_elements):
        self.parent = [i for i in range(total_elements)]
        self.total_elements = total_elements
        self.connected_components = total_elements

    def union(self, element1, element2):
        # root1, root2 = self.find(element1), self.find(element2)
        root1, root2 = self.parent[element1], self.parent[element2]
        if root1 != root2:
            self.connected_components -= 1
            self.parent[root2] = root1

    # def find(self, element):
    #     if element != self.parent[element]:
    #         self.parent[element] = self.find(self.parent[element])
    #     return self.parent[element]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        island_dict = dict()
        total_elements = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    island_dict[i, j] = total_elements
                    total_elements += 1
        union_find = UnionFind(total_elements)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    if i > 0 and grid[i - 1][j] == '1':
                        union_find.union(island_dict[i - 1, j], island_dict[i, j])
                    if j > 0 and grid[i][j - 1] == '1':
                        union_find.union(island_dict[i, j - 1], island_dict[i, j])
        return union_find.connected_components


if __name__ == '__main__':

    # Inputs and Expected Outputs
    grid_1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    expected_output_1 = 1

    grid_2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    expected_output_2 = 3

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.numIslands(grid_1)
    test_2 = solution_2.numIslands(grid_2)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
