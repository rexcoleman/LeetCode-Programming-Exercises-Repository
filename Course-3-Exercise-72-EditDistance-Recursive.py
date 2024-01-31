class Solution:
    def minDistance(self, w1: str, w2: str) -> int:

        def minDistanceRecur(w1, w2, n, m):

            if n == 0 or m == 0:
                return m or n
            elif w1[n - 1] == w2[m - 1]:
                return minDistanceRecur(w1, w2, n - 1, m - 1)
            else:
                return 1 + min(
                    minDistanceRecur(w1, w2, n - 1, m - 1),
                    minDistanceRecur(w1, w2, n, m - 1),
                    minDistanceRecur(w1, w2, n - 1, m)
                )


        return minDistanceRecur(w1, w2, len(w1), len(w2))


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