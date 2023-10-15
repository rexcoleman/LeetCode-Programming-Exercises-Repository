

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 2:
            x0 = x1
            x1 = (x0 + x / x0) / 2
        return int(x1)


if __name__ == '__main__':
    # Inputs
    x1 = 4
    x2 = 1000

    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.mySqrt(x1)
    test_2 = solution_2.mySqrt(x2)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")