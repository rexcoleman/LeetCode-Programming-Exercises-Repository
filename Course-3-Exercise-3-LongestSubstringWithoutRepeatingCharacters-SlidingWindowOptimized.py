from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        n = len(string)
        answer = 0
        # mp stores the current index of a character
        mp ={}
        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if string[j] in mp:
                i = max(mp[string[j]], i)

            answer = max(answer, j - i + 1)

            # If string[j] is already in mp, it means you've encountered this character before.
            # In this case, you want to update the starting index i to be the next index of string[j].
            # By doing i = max(mp[string[j]], i), you're making sure that i always points to the
            # next index where you can start a new substring without repeating characters.
            mp[string[j]] = j + 1
        return answer


if __name__ == '__main__':

    # Inputs
    s1 = "abcabcbb"
    s2 = "abba"
    s3 = "pwwkew"

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()

    test_1 = solution_1.lengthOfLongestSubstring(s1)
    test_2 = solution_2.lengthOfLongestSubstring(s2)
    test_3 = solution_3.lengthOfLongestSubstring(s3)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")
    print(f"Test 3: {test_3}")

    # Expected Outputs: Output1-3, Output2-1, Output3-3
