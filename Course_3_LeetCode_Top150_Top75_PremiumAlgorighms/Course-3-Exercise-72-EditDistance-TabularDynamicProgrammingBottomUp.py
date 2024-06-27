class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1); n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base Case 0th row where len(word1) = 0
        for i in range (n + 1):
            dp[0][i] = i

        # Base Case 0th column where len(word2) = 0
        for j in range(m + 1):
            dp[j][0] = j

        for j in range(1, m + 1):
            for i in range(1, n + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[j][i] = dp[j - 1][i - 1]
                else:
                    dp[j][i] = 1 + min(
                        dp[j - 1][i - 1],   # Replace
                        dp[j - 1][i],       # Delete
                        dp[j][i - 1]        # Insert
                    )



        return dp[-1][-1]



if __name__ == '__main__':

    # Inputs and Expected Outputs
    word1_1 = "horse"
    word1_2 = "ros"
    expected_output_1 = 3
    word2_1 = "intention"
    word2_2 = "execution"
    expected_output_2 = 5

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.minDistance(word1_1, word1_2)
    test_2 = solution_2.minDistance(word2_1, word2_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")

    # Assert Tests
    assert test_1 == expected_output_1, f"Test failed: Expected {expected_output_1}, got {test_1}"
    assert test_2 == expected_output_2, f"Test failed: Expected {expected_output_2}, got {test_2}"
    assert solution_3.minDistance("", "abc") == 3  # Requires three inserts
    assert solution_3.minDistance("abc", "") == 3  # Requires three deletes
    assert solution_3.minDistance("", "") == 0  # Both strings are empty
    assert solution_3.minDistance("same", "same") == 0  # No operations needed
    assert solution_3.minDistance("a", "b") == 1  # One replace
    assert solution_3.minDistance("ab", "a") == 1  # One delete
    assert solution_3.minDistance("a", "ab") == 1  # One insert
    assert solution_3.minDistance("Abc", "abc") == 1  # One replace (if case-sensitive)

    # If the program reaches this point, the assertions passed
    print("\nAll tests passed successfully.")
