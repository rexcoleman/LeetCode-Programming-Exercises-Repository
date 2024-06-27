from collections import deque
from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                # Handle out of bounds case
                if i < len(word) - 1:
                    continue

                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1: i + 1] == word:
                        dp[i] = True
                        break
        return dp[-1]





if __name__ == '__main__':

    # Inputs and Expected Outputs
    s_1 = "leetcode"
    wordDict_1 = ["leet", "code"]
    expected_output_1 = True
    s_2 = "applepenapple"
    wordDict_2 = ["apple", "pen"]
    expected_output_2 = True
    s_3 = "catsandog"
    wordDict_3 = ["cats", "dog", "sand", "and", "cat"]
    expected_output_3 = False

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.wordBreak(s_1, wordDict_1)
    test_2 = solution_2.wordBreak(s_2, wordDict_2)
    test_3 = solution_3.wordBreak(s_3, wordDict_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \n Expected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \n Expected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \n Expected Output: {expected_output_3}")