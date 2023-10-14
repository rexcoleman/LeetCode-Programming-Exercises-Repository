
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_num = 0
        temp = x
        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10
        return reversed_num == x


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