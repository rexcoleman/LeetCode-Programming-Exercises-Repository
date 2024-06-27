from collections import defaultdict, Counter


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if k >= n:
            return n
        left, right = k, n

        def isValid(size):
            counter = Counter(s[:size])
            if len(counter) <= k:
                return True
            for i in range(size, n):
                counter[s[i]] += 1
                counter[s[i - size]] -= 1
                if counter[s[i - size]] == 0:
                    del counter[s[i - size]]
                if len(counter) <= k:
                    return True
            return False

        while left < right:
            mid = (left + right + 1) // 2

            if isValid(mid):
                left = mid
            else:
                right = mid - 1

        return left


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