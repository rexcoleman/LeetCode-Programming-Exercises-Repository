from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        cols = 0
        rows = len(words)
        new_words = []

        for word in words:
            cols = max(cols, len(word))

        # If the first row doesn't have maximum number of characters, or
        # the number of rows is not equal to columns it can't form a square.

        if cols != len(words[0]) or rows != cols:
            return False

        for col in range(cols):
            new_word = []

            # Iterate on each character of column 'col'.
            for row in range(rows):
                # If the current row's word's size is less than the column number it means this column is empty,
                # or, if there is a character present then use it to make the new word.
                if col < len(words[row]):
                    new_word.append(words[row][col])

            # Push the new word of column 'col' in the list.
            new_words.append(''.join(new_word))

        # Check if all row's words match with the respective column's words.
        return words == new_words


if __name__ == '__main__':

    # Inputs and Expected Outputs
    words_1 = ["abcd", "bnrt", "crmy", "dtye"]
    expected_output_1 = True
    words_2 = ["abcd", "bnrt", "crm", "dt"]
    expected_output_2 = True
    words_3 = ["ball", "area", "read", "lady"]
    expected_output_3 = False
    words_4 = ["abc","b","c"]
    expected_output_4 = True

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    test_1 = solution_1.validWordSquare(words_1)
    test_2 = solution_2.validWordSquare(words_2)
    test_3 = solution_3.validWordSquare(words_3)
    test_4 = solution_4.validWordSquare(words_4)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
    print(f"\nTest 4 Output: {test_4} \nExpected Output: {expected_output_4}")