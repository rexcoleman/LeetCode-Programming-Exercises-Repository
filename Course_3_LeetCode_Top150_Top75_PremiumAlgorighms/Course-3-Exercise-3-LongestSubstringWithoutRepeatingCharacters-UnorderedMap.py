
class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        length = len(string)
        max_length = 0
        char_map = {}
        left_pointer = 0

        for right_pointer in range(length):
            if string[right_pointer] not in char_map or char_map[string[right_pointer]] < left_pointer:
                char_map[string[right_pointer]] = right_pointer
                max_length = max(max_length, right_pointer - left_pointer + 1)
            else:
                left_pointer = char_map[string[right_pointer]] + 1
                char_map[string[right_pointer]] = right_pointer
        return max_length


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
