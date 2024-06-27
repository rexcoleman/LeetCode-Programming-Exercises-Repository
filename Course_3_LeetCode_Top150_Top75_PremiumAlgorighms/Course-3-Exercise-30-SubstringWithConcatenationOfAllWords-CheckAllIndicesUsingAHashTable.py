from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = Counter(words)

        def check(i):
            # Copy the original dictionary to use for this index
            remaining = word_count.copy()
            words_used = 0

            # Each iteration will check for a match in words
            for j in range(i, i + substring_size, word_length):
                sub = s[j: j + word_length]
                if remaining[sub] > 0:
                    remaining[sub] -= 1
                    words_used += 1
                else:
                    break

            # Valid if we used all the words
            return words_used == k

        answer = []
        for i in range(n - substring_size + 1):
            if check(i):
                answer.append(i)

        return answer


if __name__ == '__main__':

    # Inputs and Expected Outputs
    s_1 = "barfoothefoobarman"
    words_1 = ["foo", "bar"]
    expected_output_1 = [0, 9]
    s_2 = "wordgoodgoodgoodbestword"
    words_2 = ["word", "good", "best", "word"]
    expected_output_2 = []
    s_3 = "barfoofoobarthefoobarman"
    words_3 = ["bar", "foo", "the"]
    expected_output_3 = [6, 9, 12]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.findSubstring(s_1, words_1)
    test_2 = solution_2.findSubstring(s_2, words_2)
    test_3 = solution_3.findSubstring(s_3, words_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")