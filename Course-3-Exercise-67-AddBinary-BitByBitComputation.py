

class Solution:
    def addBinary(self, a, b) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        carry = 0
        answer = []
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')

            carry //= 2

        if carry == 1:
            answer.append('1')
        answer.reverse()

        return ''.join(answer)

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
