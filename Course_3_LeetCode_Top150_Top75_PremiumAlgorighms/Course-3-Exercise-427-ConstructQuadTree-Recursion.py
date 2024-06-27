from collections import deque
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.helper(grid, 0, 0, len(grid))

    def helper(self, grid, i, j, w):
        if self.allSame(grid, i, j, w):
            return Node(grid[i][j] == 1, True)
        node = Node(True, False)
        node.topLeft = self.helper(grid, i, j, w // 2)
        node.topRight = self.helper(grid, i, j + w // 2, w // 2)
        node.bottomLeft = self.helper(grid, i + w // 2, j, w // 2)
        node.bottomRight = self.helper(grid, i + w // 2, j + w // 2, w // 2)
        return node



    def allSame(self, grid, i, j, w):
        for x in range(i, i + w):
            for y in range(j, j + w):
                if grid[x][y] != grid[i][j]:
                    return False
        return True


def quadTreeToList(root):
    output = []
    if not root:
        return output
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current is not None:
            output.append([int(current.isLeaf), int(current.val)])
            queue.append(current.topLeft)
            queue.append(current.topRight)
            queue.append(current.bottomLeft)
            queue.append(current.bottomRight)
        else:
            output.append(None)
    while output and output[-1] is None:
        output.pop()
    return output





if __name__ == '__main__':

    # Inputs and Expected Outputs
    grid_1 = [[0, 1], [1, 0]]
    expected_output_1 = [[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]]
    grid_2 = [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0]
    ]
    expected_output_2 = [
        [0, 1], [1, 1], [0, 1], [1, 1],
        [1, 0], None, None, None, None,
        [1, 0], [1, 0], [1, 1], [1, 1]
    ]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.construct(grid_1)
    test_2 = solution_2.construct(grid_2)

    # Print Results
    output_1 = quadTreeToList(test_1)
    output_2 = quadTreeToList(test_2)
    print(f"\nTest 1 Result {output_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result {output_2} \nExpected Result: {expected_output_2}")
