from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0

        ret, up, down, peak = 1, 0, 0, 0
        for prev, curr in zip(ratings[:-1], ratings[1:]):
            if prev < curr:
                up, down, peak = up + 1, 0, up + 1
                ret += 1 + up
            elif prev == curr:
                up = down = peak = 0
                ret += 1
            else:
                up, down = 0, down + 1
                a = int(peak >= down)
                ret += 1 + down - int(peak >= down)

        return ret

if __name__ == '__main__':

    # Inputs and Expected Outputs
    ratings_1 = [1, 0, 2]
    expected_output_1 = 5
    ratings_2 = [1, 2, 3, 3, 2, 1]
    expected_output_2 = 12

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