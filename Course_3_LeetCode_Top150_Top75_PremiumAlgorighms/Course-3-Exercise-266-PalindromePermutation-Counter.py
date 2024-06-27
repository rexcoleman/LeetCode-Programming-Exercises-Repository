import collections
from collections import defaultdict, Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        char_count = Counter(s)
        odd_counter = sum(1 for char in char_count if char_count[char] % 2)
        return odd_counter < 2

        # return sum(v % 2 for v in collections.Counter(s).values()) < 2


if __name__ == '__main__':

    # Inputs and Expected Outputs
    s_1 = "code"
    expected_output_1 = False
    s_2 = "aab"
    expected_output_2 = True
    s_3 = "carerac"
    expected_output_3 = True

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.canPermutePalindrome(s_1)
    test_2 = solution_2.canPermutePalindrome(s_2)
    test_3 = solution_3.canPermutePalindrome(s_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")

