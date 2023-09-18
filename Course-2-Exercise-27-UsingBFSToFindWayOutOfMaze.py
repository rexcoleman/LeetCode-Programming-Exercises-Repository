from collections import deque

class MazeSolver:

    def __init__(self, matrix):

        self.matrix = matrix
        # D(0,1), U(0,-1), L(-1,0), R(1,0)
        self.move_x = [1, 0, 0, -1]
        self.move_y = [0, -1, 1, 0]
        self.visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix))]
        self.min_distance = float('inf')

    def is_valid(self, row, col):

        # outside the table horizontally
        if row < 0 or row >= len(self.matrix):
            return False

        # outside the table vertically
        if col < 0 or col >= len(self.matrix):
            return False

        # obstacle (wall)
        if self.matrix[row][col] == 0:
            return False

        # already visited the given cell
        if self.visited[row][col]:
            return False

        return True

    def search(self, i, j, destination_x, destination_y):

        self.visited[i][j] = True
        # the queue is implemented with a doubly linked list - O(1)
        queue = deque()
        # i is the x coordinate
        # j is the y coordinate
        # why 0? in the first iteration the minimum distance is 0
        queue.append((i, j, 0))

        while queue:

            # we take out the first item we have inserted
            (i, j, dist) = queue.popleft()

            # if we have reached the destination - we break out of the while loop because we have
            # found the destination!!!
            if i == destination_x and j == destination_y:
                self.min_distance = dist
                break

            # we are at the location (i, j) we have to make a given move
            # L, U, R, D
            for move in range(len(self.move_x)):
                # we calculate the position after the move
                next_x = i + self.move_x[move]
                next_y  = j + self.move_y[move]

                # is it possible to make the move with coordinates (next_x, next_y)?
                if self.is_valid(next_x, next_y):
                    # we make the give move (BFS)
                    self.visited[next_x][next_y] = True
                    # we append the move to the queue
                    queue.append((next_x, next_y, dist + 1))

    def show_result(self):

        if self.min_distance != float('inf'):
            print('The shortest path from source to destination: ', self.min_distance)
        else:
            print('No feasible solution - the destination cannot be reached!')




if __name__ == '__main__':

    m = [
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1],
        [0, 0, 0, 1, 1],
    ]

    maze_solver = MazeSolver(m)
    maze_solver.search(0, 0, 4, 4)
    maze_solver.show_result()