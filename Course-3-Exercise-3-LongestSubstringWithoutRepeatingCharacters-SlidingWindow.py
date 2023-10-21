from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        chars = Counter()
        left = right = 0
        result = 0

        while right < len(string):
            r = string[right]
            chars[r] += 1

            while chars[r] > 1:
                l = string[left]
                chars[l] -= 1
                left += 1

            result = max(result, right - left + 1)
            right += 1
        return result


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
