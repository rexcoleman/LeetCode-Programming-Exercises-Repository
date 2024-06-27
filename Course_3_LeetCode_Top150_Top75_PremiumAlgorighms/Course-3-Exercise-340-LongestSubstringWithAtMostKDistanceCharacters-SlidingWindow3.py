from collections import defaultdict, Counter


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n <= k:
            return n
        max_size = 0
        counter = Counter()
        left = 0
        for right in range(n):
            counter[s[right]] += 1

            if len(counter) <= k:
                max_size += 1
            else:
                counter[s[right - max_size]] -= 1
                if counter[s[right - max_size]] == 0:
                    del counter[s[right - max_size]]

        return max_size


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