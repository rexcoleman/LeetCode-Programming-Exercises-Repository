from collections import defaultdict


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        n = len(s)
        if k > n:
            return 0
        substrings = 0
        char_map = defaultdict(int)
        left = right = 0
        while right < n:
            while s[right] in char_map:
                del char_map[s[left]]
                left += 1
            char_map[s[right]] += 1
            right += 1
            if right - left == k:
                del char_map[s[left]]
                left += 1
                substrings += 1
        return substrings


if __name__ == '__main__':

    # Inputs and Expected Outputs
    s_1 = "havefunonleetcode"
    k_1 = 5
    expected_output_1 = 6
    s_2 = "home"
    k_2 = 5
    expected_output_2 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.numKLenSubstrNoRepeats(s_1, k_1)
    test_2 = solution_2.numKLenSubstrNoRepeats(s_2, k_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
