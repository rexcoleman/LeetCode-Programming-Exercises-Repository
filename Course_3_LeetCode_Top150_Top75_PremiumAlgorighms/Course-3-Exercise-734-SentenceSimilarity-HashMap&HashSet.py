from collections import defaultdict
from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        wordToSimilarWords = defaultdict(set)

        for word1, word2 in similarPairs:
            wordToSimilarWords[word1].add(word2)
            wordToSimilarWords[word2].add(word1)

        for i, (s1, s2) in enumerate(zip(sentence1, sentence2)):
            if s1 == s2 or s2 in wordToSimilarWords[s1]:
                continue
            return False

        return True


if __name__ == '__main__':

    # Inputs and Expected Outputs
    sentence1_1 = ["great", "acting", "skills"]
    sentence2_1 = ["fine", "drama", "talent"]
    similarPairs_1 = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]
    expected_output_1 = True
    sentence1_2 = ["great"]
    sentence2_2 = ["great"]
    similarPairs_2 = []
    expected_output_2 = True
    sentence1_3 = ["great"]
    sentence2_3 = ["doubleplus", "good"]
    similarPairs_3 = [["great", "doubleplus"]]
    expected_output_3 = False

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.areSentencesSimilar(sentence1_1, sentence2_1, similarPairs_1)
    test_2 = solution_2.areSentencesSimilar(sentence1_2, sentence2_2, similarPairs_2)
    test_3 = solution_3.areSentencesSimilar(sentence1_3, sentence2_3, similarPairs_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")

