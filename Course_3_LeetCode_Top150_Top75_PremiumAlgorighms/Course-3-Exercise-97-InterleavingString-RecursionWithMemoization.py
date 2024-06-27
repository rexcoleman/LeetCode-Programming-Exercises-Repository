class Solution:
    def interLeave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False

        memo = {}

        def helper(i: int, j: int, k: int) -> bool:
            if k == l:
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            ans = False
            if i < m and s1[i] == s3[k]:
                ans = ans or helper(i + 1, j, k + 1)

            if j < n and s2[j] == s3[k]:
                ans = ans or helper(i, j + 1, k + 1)

            memo[(i, j)] = ans
            return ans


        return helper(0, 0, 0)


if __name__ == '__main__':

    # Inputs and Expected Outputs
    s1_1 = "aabcc"
    s1_2 = "dbbca"
    s1_3 = "aadbbcbcac"
    expected_output_1 = True
    s2_1 = "aabcc"
    s2_2 = "dbbca"
    s2_3 = "aadbbbaccc"
    expected_output_2 = False
    s3_1 = ""
    s3_2 = ""
    s3_3 = ""
    expected_output_3 = True

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.interLeave(s1_1, s1_2, s1_3)
    test_2 = solution_2.interLeave(s2_1, s2_2, s2_3)
    test_3 = solution_3.interLeave(s3_1, s3_2, s3_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")

