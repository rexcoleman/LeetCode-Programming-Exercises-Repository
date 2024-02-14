class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        len_diff = abs(len_s - len_t)
        distance = 0
        if len_diff >= 2:
            return False
        if len_diff == 1 and (len_s == 0 or len_t == 0):
            return True
        if len_t < len_s:
            return self.isOneEditDistance(t, s)

        for i in range(len_s):
            if s[i] != t[i]:
                if len_diff == 0:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]

        # If there are no diffs in the distance
        # The strings are one edit away only if
        # t has one more character.
        return len_s + 1 == len_t


if __name__ == '__main__':

    # Inputs and Expected Outputs
    s_1 = "ab"
    t_1 = "acb"
    expected_output_1 = True
    s_2 = ""
    t_2 = ""
    expected_output_2 = False
    s_3 = "ba"
    t_3 = "a"
    expected_output_3 = True

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.isOneEditDistance(s_1, t_1)
    test_2 = solution_2.isOneEditDistance(s_2, t_2)
    test_3 = solution_3.isOneEditDistance(s_3, t_3)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")