from typing import List


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m, n = len(picture), len(picture[0])
        col = [0] * n
        row = set()
        for i in range(m):
            cnt = 0
            for j in range(n):
                if picture[i][j] == 'B':
                    c = j
                    cnt += 1
                    col[j] += 1
            if cnt == 1: row.add(c)
        ans = 0
        for i, c in enumerate(col):
            if c == 1 and i in row:
                ans += 1
        return ans


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