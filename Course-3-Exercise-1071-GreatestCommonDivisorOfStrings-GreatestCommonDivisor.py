from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths.
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]


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



