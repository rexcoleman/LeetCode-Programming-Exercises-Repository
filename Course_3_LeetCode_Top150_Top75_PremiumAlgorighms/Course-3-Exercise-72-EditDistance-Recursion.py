class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def solve(word1, word2, m, n):
            # Base Case if any one of w1 or w2 is empty
            if m == 0 or n == 0:
                return m or n

            elif word1[m - 1] == word2[n - 1]:
                return solve(word1, word2, m - 1, n - 1)

            else:
                return 1 + min(
                    solve(word1, word2, m - 1, n - 1),
                    solve(word1, word2, m - 1, n),
                    solve(word1, word2, m, n - 1)
                )

        return solve(word1, word2, len(word1), len(word2))

    # Time Limit Exceeded
    # We need to use Memoization in this Solution to avoid repetative same calculation of sub-problems


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
