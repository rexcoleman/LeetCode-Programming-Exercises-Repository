
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]




if __name__ == '__main__':

    # Inputs
    x1 = 121
    x2 = -121
    x3 = 10

    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()

    test_1 = solution_1.isPalindrome(x1)
    test_2 = solution_2.isPalindrome(x2)
    test_3 = solution_3.isPalindrome(x3)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")
    print(f"Test 3: {test_3}")