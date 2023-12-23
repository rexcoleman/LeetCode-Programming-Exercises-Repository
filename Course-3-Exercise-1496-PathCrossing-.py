class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        current = (0, 0)
        visited.add(current)
        traverse = {
            'N': [-1, 0],
            'E': [0, 1],
            'S': [1, 0],
            'W': [0,-1]
        }
        for step in path:
            x, y = traverse[step]
            current = (current[0] + x, current[1] + y)
            if current in visited:
                return True
            else:
                visited.add(current)
        return False


if __name__ == '__main__':

    # Inputs and Expected Outputs
    path_1 = "NES"
    expected_output_1 = False
    path_2 = "NESWW"
    expected_output_2 = True

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.isPathCrossing(path_1)
    test_2 = solution_2.isPathCrossing(path_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")

