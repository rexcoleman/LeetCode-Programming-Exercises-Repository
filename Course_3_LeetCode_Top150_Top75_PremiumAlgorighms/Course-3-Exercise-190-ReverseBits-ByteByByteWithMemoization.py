

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 24
        cache = dict()
        while n:
            ret += self.reverserByte(n & 0xff, cache) << power
            n = n >> 8
            power -= 8
        return ret

    def reverserByte(self, byte, cache):
        if byte not in cache:
            cache[byte] = (byte * 0x0202020202 & 0x010884422010) % 1023
        return cache[byte]








if __name__ == '__main__':

    # Inputs
    n1 = 0b00000010100101000001111010011100
    n2 = 0b11111111111111111111111111111101

    bin_n_1 = bin(0x0202020202)[2:]
    # print(bin_n_1)
    bin_n_2 = bin(0x010884422010)[2:]
    # print(bin_n_2)

    # Expected Outputs:
    # 1: 964176192
    # 2: 3221225471

    test_1 = Solution()
    test_2 = Solution()

    t_1 = test_1.reverseBits(n1)
    t_2 = test_2.reverseBits(n2)

    print(f"Test 1: {t_1}")
    print(f"Test 2: {t_2}")


    #
    # def reverserByte(self, byte, cache):
    #     if byte not in cache:
    #         print(bin(byte))
    #         print(bin_n_1)
    #         print(bin(byte * 0x0202020202))
    #         print(bin_n_2)
    #         print(bin(byte * 0x0202020202 & 0x010884422010))
    #         cache[byte] = (byte * 0x0202020202 & 0x010884422010) % 1023
    #         print(bin(cache[byte]))
    #     return cache[byte]
