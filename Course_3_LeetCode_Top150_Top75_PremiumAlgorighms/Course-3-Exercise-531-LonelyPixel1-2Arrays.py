from typing import List


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:

        rows_count = [0] * len(picture)
        cols_count = [0] * len(picture[0])
        lonely_pixels = 0

        for row in range(len(picture)):
            for col in range(len(picture[0])):
                if picture[row][col] == "B":
                    rows_count[row] += 1
                    cols_count[col] += 1

        for row in range(len(picture)):
            for col in range(len(picture[0])):
                if picture[row][col] == "B":
                    if rows_count[row] == 1 and cols_count[col] == 1:
                        lonely_pixels += 1

        return lonely_pixels


if __name__ == '__main__':

    # Inuts and Expected Outputs
    picture_1 = [["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]]
    expected_output_1 = 3
    picture_2 = [["B", "B", "B"], ["B", "B", "W"], ["B", "B", "B"]]
    expected_output_2 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.findLonelyPixel(picture_1)
    test_2 = solution_2.findLonelyPixel(picture_2)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")