class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            bin_n = bin(n)
            if n & 1:
                count += 1
            n = n >> 1
        return count


if __name__ == '__main__':

    # Inputs
    n1 = 0b00000000000000000000000000001011
    n2 = 0b00000000000000000000000010000000
    n3 = 0b11111111111111111111111111111101

    test_1 = Solution()
    test_2 = Solution()
    test_3 = Solution()

    t_1 = test_1.hammingWeight(n1)
    t_2 = test_2.hammingWeight(n2)
    t_3 = test_3.hammingWeight(n3)

    print(f"Test 1: {t_1}")
    print(f"Test 2: {t_2}")
    print(f"Test 3: {t_3}")
