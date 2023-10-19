from math import ceil


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        answer = []
        n = len(s)
        charsInSection = (2 * numRows) - 2
        for currRow in range(numRows):
            index = currRow
            while index < n:
                answer.append(s[index])
                # If currRow is not the first or last row,
                # then we add one more character from the current section
                if currRow != 0 and currRow != numRows - 1:
                    charsInBetween = charsInSection - (2 * currRow)
                    secondIndex = index + charsInBetween

                    if secondIndex < n:
                        answer.append(s[secondIndex])
                # Jump to same row's first character in next section
                index += charsInSection

        return ''.join(answer)





if __name__ == '__main__':

    # Inputs
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    expectedAnswer1 = "PAHNAPLSIIGYIR"
    s2 = "PAYPALISHIRING"
    numRows2 = 4
    expectedAnswer2 = "PINALSIGYAHRPI"
    s3 = "A"
    numRows3 = 1
    expectedAnswer3 = "A"

    # Run tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()

    test_1 = solution_1.convert(s1, numRows1)
    test_2 = solution_2.convert(s2, numRows2)
    test_3 = solution_3.convert(s3, numRows3)

    print(f"Test 1: {test_1}")
    print(test_1 == expectedAnswer1)
    print(f"Test 2: {test_2}")
    print(test_2 == expectedAnswer2)
    print(f"Test 3: {test_3}")
    print(test_3 == expectedAnswer3)