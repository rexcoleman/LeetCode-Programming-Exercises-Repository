from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def valid(k):
            if len1 % k or len2 % k:
                return False
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            return str1 == n1 * base and str2 == n2 * base

        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""


if __name__ == '__main__':

    # Inputs and Expected Outputs
    str1_1 = "ABCABC"
    str2_1 = "ABC"
    expected_output_1 = "ABC"
    str1_2 = "ABABAB"
    str2_2 = "ABAB"
    expected_output_2 = "AB"
    str1_3 = "LEET"
    str2_3 = "CODE"
    expected_output_3 = ""

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.gcdOfStrings(str1_1, str2_1)
    test_2 = solution_2.gcdOfStrings(str1_2, str2_2)
    test_3 = solution_3.gcdOfStrings(str1_3, str2_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")



