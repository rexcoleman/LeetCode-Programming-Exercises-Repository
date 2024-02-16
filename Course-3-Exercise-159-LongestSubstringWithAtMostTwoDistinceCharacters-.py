from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        longest = 0
        count = defaultdict(int)
        set_s = set()
        len_s = len(s)
        left = right = 0
        while left < len_s:
            set_s.add(s[right])
            count[s[right]] += 1
            while len(set_s) > 2:
                longest = max(longest, right - left)
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    set_s.remove(s[left])
                left += 1
            if right < len_s - 1:
                right += 1
            else:
                longest = max(longest, right - left + 1)
                left += 1
        return longest


if __name__ == '__main__':

    # Inputs and Expected Outputs
    s_1 = "eceba"
    expected_output_1 = 3
    s_2 = "ccaabbb"
    expected_output_2 = 5

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.lengthOfLongestSubstringTwoDistinct(s_1)
    test_2 = solution_2.lengthOfLongestSubstringTwoDistinct(s_2)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
