import heapq
from collections import deque
from typing import List



class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board_size = len(board)
        # cells provides the coordinates in the matrix for each move of the dice roll (curr + dice roll)
        # we have 37 values because the graph starts at node 1
        position_coordinates = [None] * (board_size ** 2 + 1)
        # label is used to advance the index in cells with each iteration
        cell_index = 1
        columns = list(range(0, board_size))
        for row in range(board_size - 1, -1, -1):
            for column in columns:
                position_coordinates[cell_index] = (row, column)
                cell_index += 1
            # the reverse list method is used to manage the boustrophedon style of the graph
            # (left to right then right to left)
            columns.reverse()
        # Min_roll_to_reach_node keeps track of the minimum number of rolls required to reach each node
        # and it updates each value via breadth first search using queue
        # we have 37 values because the graph starts at node 1
        min_roll_to_reach_node = [-1] * (board_size * board_size + 1)
        min_roll_to_reach_node[1] = 0
        priority_queue = [(0, 1)]
        while priority_queue:
            current_distance, current_cell = heapq.heappop(priority_queue)
            # the conditional makes sure we don't overwrite a smaller value with a larger value
            # if we already reached this cell then we assume the min roll < current_distance
            # this is enforced by the priority queue
            if current_distance != min_roll_to_reach_node[current_cell]:
                continue
            # the +1 in min(curr + 6, n**2) + 1 is used to account for the range method
            # not being inclusive of the second value
            for next_cell in range(current_cell + 1, min(current_cell + 6, board_size ** 2) + 1):
                row, column = position_coordinates[next_cell]
                # this condition considers snakes and ladders
                target_cell = board[row][column] if board[row][column] != -1 else next_cell
                # this conditional tests if we need to update the min_roll_to_reach_node value
                # for the target cell.  If it is -1 then this is our first time reaching this cell
                # and we update it.  The second part is the magic of dijkstras algo where we are looking
                # for the shortest path to a cell
                if min_roll_to_reach_node[target_cell] == -1 or \
                        min_roll_to_reach_node[current_cell] + 1 < min_roll_to_reach_node[target_cell]:
                    min_roll_to_reach_node[target_cell] = min_roll_to_reach_node[current_cell] + 1
                    heapq.heappush(priority_queue, (min_roll_to_reach_node[target_cell], target_cell))
        return min_roll_to_reach_node[board_size * board_size]





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