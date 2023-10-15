

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)


if __name__ == '__main__':

    # Inputs
    n1 = 2
    n2 = 3

    # Run tests
    test_1 = Solution()
    test_2 = Solution()

    t_1 = test_1.climbStairs(n1)
    t_2 = test_2.climbStairs(n2)

    print(f"Test 1: {t_1}")
    print(f"Test 2: {t_2}")
