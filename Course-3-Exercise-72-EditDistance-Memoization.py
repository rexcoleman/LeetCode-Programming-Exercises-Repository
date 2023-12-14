class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dfs(i, j):
            if i == 0 or j == 0:
                return i or j

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i - 1] == word2[j - 1]:
                ans = dfs(i -1, j - 1)

            else:
                ans = 1 + min(dfs(i - 1, j - 1), dfs(i - 1, j), dfs(i, j - 1))

            memo[(i, j)] = ans
            return memo[(i, j)]

        return dfs(len(word1), len(word2))


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
    test_1 = solution_1.minDistance(word1_1, word1_2)
    test_2 = solution_2.minDistance(word2_1, word2_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
