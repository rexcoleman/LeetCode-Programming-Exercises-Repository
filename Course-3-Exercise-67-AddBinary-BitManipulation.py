

class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]



if __name__ == '__main__':

    # Inputs
    a1 = "11"
    b1 = "1"
    a2 = "1010"
    b2 = "1011"

    test_1 = Solution()
    test_2 = Solution()

    t_1 = test_1.addBinary(a1, b1)
    t_2 = test_2.addBinary(a2, b2)

    print(f"Test 1: {t_1}")
    print(f"Test 2: {t_2}")