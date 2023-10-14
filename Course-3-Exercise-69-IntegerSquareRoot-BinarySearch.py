from math import e, log

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 2, x // 2
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
        return right



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