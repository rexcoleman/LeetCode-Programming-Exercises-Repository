from math import e, log

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = int(e**(0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right


if __name__ == '__main__':
    # Inputs
    x1 = 4
    x2 = 8

    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.mySqrt(x1)
    test_2 = solution_2.mySqrt(x2)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")