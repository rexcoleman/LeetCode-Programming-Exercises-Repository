class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slow, fast = 0, 0
        len_s, len_t = len(s), len(t)
        for slow in range(len_s):
            while fast < len_t:
                if t[fast] == s[slow]:
                    slow += 1
                    if slow == len_s:
                        return True
                fast += 1
        return slow >= len_s







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