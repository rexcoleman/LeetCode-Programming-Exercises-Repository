
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret




if __name__ == '__main__':

    # Inputs
    n1 = 0b00000010100101000001111010011100
    n2 = 0b11111111111111111111111111111101

    # Expected Outputs:
    # 1: 964176192
    # 2: 3221225471

    test_1 = Solution()
    test_2 = Solution()

    t_1 = test_1.reverseBits(n1)
    t_2 = test_2.reverseBits(n2)

    print(f"Test 1: {t_1}")
    print(f"Test 2: {t_2}")
