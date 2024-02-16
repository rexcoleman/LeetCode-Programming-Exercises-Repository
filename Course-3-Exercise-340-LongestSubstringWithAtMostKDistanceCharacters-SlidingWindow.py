from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n <= k:
            return n
        max_len = 0
        count_map = defaultdict(int)
        left, right = 0, 0

        while right < n:
            count_map[s[right]] = right
            right += 1
            if len(count_map) == k + 1:
                del_idx = min(count_map.values())
                del count_map[s[del_idx]]
                left = del_idx + 1
            max_len = max(max_len, right - left)

        return max_len

if __name__ == '__main__':

    # Inputs and Expected Outputs
    s_1 = "eceba"
    k_1 = 2
    expected_output_1 = 3
    s_2 = "aa"
    k_2 = 1
    expected_output_2 = 2

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.lengthOfLongestSubstringKDistinct(s_1, k_1)
    test_2 = solution_2.lengthOfLongestSubstringKDistinct(s_2, k_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")