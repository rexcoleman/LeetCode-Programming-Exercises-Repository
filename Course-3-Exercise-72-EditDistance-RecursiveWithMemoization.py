class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        n, m = len(w1), len(w2)

        dp = [[0] * (m+1) for i in range(n+1)]

        for j in range(m+1): # Base Case 0th row where len(w1) = 0
            dp[0][j] = j

        for i in range(n+1):  # Base Case 0th column where len(w2) = 0
            dp[i][0] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if w1[i-1] == w2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j-1],  # Replace
                        dp[i-1][j],  # Delete
                        dp[i][j-1]  # Insert
                    )

        return dp[-1][-1]


if __name__ == '__main__':

    # Inputs and Expected Outputs
    word1_1 = "horse"
    word2_1 = "ros"
    expected_output_1 = 3
    word1_2 = "intention"
    word2_2 = "execution"
    expected_output_2 = 5

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.minDistance(word1_1, word2_1)
    test_2 = solution_2.minDistance(word1_2, word2_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")