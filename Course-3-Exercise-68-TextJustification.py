from typing import List


class Solution:




    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def get_words(i):
            current_line = []
            curr_length = 0

            while i < len(words) and curr_length + len(words[i]) <= maxWidth:
                current_line.append(words[i])
                curr_length += len(words[i]) + 1
                i += 1

            return current_line

        def create_line(line, i):
            base_length = -1
            for word in line:
                base_length += len(word) + 1

            extra_spaces = maxWidth - base_length

            if len(line) == 1 or i == len(words):
                return " ".join(line) + " " * extra_spaces

            word_count = len(line) - 1
            spaces_per_word = extra_spaces // word_count
            needs_extra_space = extra_spaces % word_count

            for j in range(needs_extra_space):
                line[j] += " "

            for j in range(word_count):
                line[j] += " " * spaces_per_word

            return " ".join(line)

        ans = []
        i = 0

        while i < len(words):
            current_line = get_words(i)
            i += len(current_line)
            ans.append(create_line(current_line, i))

        return ans


if __name__ == '__main__':

    # Inputs and Expected Outputs
    words_1 = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth_1 = 16
    expected_output_1 = [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]
    words_2 = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth_2 = 16
    expected_output_2 = [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ]
    words_3 = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
             "Art", "is", "everything", "else", "we", "do"]
    maxWidth_3 = 20
    expected_output_3 = [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  "
    ]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.fullJustify(words_1, maxWidth_1)
    test_2 = solution_2.fullJustify(words_2, maxWidth_2)
    test_3 = solution_3.fullJustify(words_3, maxWidth_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")