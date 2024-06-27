
class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        def check(start, end):
            chars = set()
            for i in range(start, end + 1):
                character = string[i]
                if character in chars:
                    return False
                chars.add(character)
            return True

        length = len(string)
        result = 0
        for left_pointer in range(length):
            for right_pointer in range(left_pointer, length):
                if check(left_pointer, right_pointer):
                    result = max(result, right_pointer - left_pointer + 1)
        return result




if __name__ == '__main__':

    # Inputs
    s1 = "abcabcbb"
    s2 = "bbbbb"
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
