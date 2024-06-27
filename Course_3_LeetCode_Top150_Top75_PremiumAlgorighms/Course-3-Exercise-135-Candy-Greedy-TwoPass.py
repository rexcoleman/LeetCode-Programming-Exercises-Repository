from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)




if __name__ == '__main__':

    # Inputs and Expected Outputs
    ratings_1 = [1, 0, 2]
    expected_output_1 = 5
    ratings_2 = [1, 2, 2]
    expected_output_2 = 4

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.candy(ratings_1)
    test_2 = solution_2.candy(ratings_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")



# Constraints:
#
# n == ratings.length
# 1 <= n <= 2 * 10^4
# 0 <= ratings[i] <= 2 * 10^4