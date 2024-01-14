from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        len_rooms = len(rooms)
        def dfs(room: List[int]):
            for i in range(len(room)):
                if room[i] in visited:
                    continue
                visited.add(room[i])
                dfs(rooms[room[i]])


        dfs(rooms[0])
        return len(visited) == len_rooms



if __name__ == '__main__':

    # Inputs and Expected Outputs
    rooms_1 = [[1], [2], [3], []]
    expected_output_1 = True
    rooms_2 = [[1, 3], [3, 0, 1], [2], [0]]
    expected_output_2 = False

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.canVisitAllRooms(rooms_1)
    test_2 = solution_2.canVisitAllRooms(rooms_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 1 Output: {test_2} \nExpected Output: {expected_output_2}")