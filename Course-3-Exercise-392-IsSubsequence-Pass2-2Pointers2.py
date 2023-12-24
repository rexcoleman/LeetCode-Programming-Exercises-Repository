class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        p_left = p_right = 0
        while p_left < LEFT_BOUND and p_right < RIGHT_BOUND:
            # move both pointers or just the right pointer
            if s[p_left] == t[p_right]:
                p_left += 1
            p_right += 1
        return p_left == LEFT_BOUND


if __name__ == '__main__':

    # Inputs and Expected Outputs:
    s1 = "abc"
    t1 = "ahbgdc"
    expected_output_1 = True
    s2 = "axc"
    t2 = "ahbgdc"
    expected_output_2 = False
    s3 = "acb"
    t3 = "ahbgdc"
    expected_output_3 = False


    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.isSubsequence(s1, t1)
    test_2 = solution_2.isSubsequence(s2, t2)
    test_3 = solution_3.isSubsequence(s3, t3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")