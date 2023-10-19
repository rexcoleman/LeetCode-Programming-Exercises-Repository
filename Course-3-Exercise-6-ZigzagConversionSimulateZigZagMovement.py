from math import ceil


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        sections = ceil(n / (2 * numRows - 2.0))
        numCols = sections * (numRows - 1)

        matrix = [[' '] * numCols for i in range(numRows)]
        currRow, currCol = 0, 0
        currStringIndex = 0

        # Iterate in zig-zag pattern on matrix and fill it with string characters.
        while currStringIndex < n:
            # Move down
            while currRow < numRows and currStringIndex < n:
                matrix[currRow][currCol] = s[currStringIndex]
                currRow += 1
                currStringIndex += 1

            currRow -= 2
            currCol += 1

            # Move diagonally up and right
            while currRow > 0 and currCol < numCols and currStringIndex < n:
                matrix[currRow][currCol] = s[currStringIndex]
                currRow -= 1
                currCol += 1
                currStringIndex += 1

        answer = ''
        for row in matrix:
            answer += "".join(row)
        return answer.replace(' ', '')






if __name__ == '__main__':

    # Inputs
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    s2 = "PAYPALISHIRING"
    numRows2 = 4
    s3 = "A"
    numRows3 = 1

    # Run tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()

    test_1 = solution_1.convert(s1, numRows1)
    test_2 = solution_2.convert(s2, numRows2)
    test_3 = solution_3.convert(s3, numRows3)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")
    print(f"Test 3: {test_3}")