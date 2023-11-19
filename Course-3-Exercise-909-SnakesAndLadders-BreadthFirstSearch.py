from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        # cells provides the coordinates in the matix for each move of the dice roll (curr + dice roll)
        # we have 37 values because the graph starts at node 1
        cells = [None] * (n**2 + 1)
        # label is used to advance the index in cells with each iteration
        label = 1
        columns = list(range(0, n))
        for row in range(n - 1, -1, -1):
            for column in columns:
                cells[label] = (row, column)
                label += 1
            # the revers list method is used to manage the boustrophedon style of the graph
            # (left to right then right to left)
            columns.reverse()
        # Min_roll_to_reach_node keeps track of the the minimun number of rolls required to reach each node
        # and it updates each vale via breadth first search using queue
        # we have 37 values because the graph starts at node 1
        min_roll_to_reach_node = [-1] * (n * n + 1)
        queue = deque([1])
        min_roll_to_reach_node[1] = 0
        while queue:
            curr = queue.popleft()
            # the +1 in min(curr + 6, n**2) + 1 is used to account for the range method
            # not being inclusive of the second value
            for next in range(curr + 1, min(curr + 6, n**2) + 1):
                row, column = cells[next]
                # this condition considers snakes and ladders
                destination = (board[row][column] if board[row][column] != -1 else next)
                # this condition ensures we do not overwrite cells with larger values
                # we are searching for the min value
                if min_roll_to_reach_node[destination] == -1:
                    min_roll_to_reach_node[destination] = min_roll_to_reach_node[curr] + 1
                    queue.append(destination)
        return min_roll_to_reach_node[n * n]





if __name__ == '__main__':

    # Inputs and Expected Outputs
    board_1 = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]
    ]
    expedcted_output_1 = 4
    board_2 = [
        [-1, -1],
        [-1, 3]
    ]
    expedcted_output_2 = 1

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.snakesAndLadders(board_1)
    test_2 = solution_2.snakesAndLadders(board_2)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expedcted_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expedcted_output_2}")