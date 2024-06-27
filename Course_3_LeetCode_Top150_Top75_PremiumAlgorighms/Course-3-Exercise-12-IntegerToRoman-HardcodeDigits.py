class Solution:
    def intToRoman(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        print(num)
        print(num // 1000)
        print(num % 1000)
        print(num % 1000 // 100)
        print(num % 100)
        print(num % 100 // 10)
        print(num % 10)

        # print(thousands[num // 1000])
        # print(hundreds[num % 1000 // 100])
        # print(tens[num % 100 // 10])
        # print(ones[num % 10])
        return (thousands[num // 1000] + hundreds[num % 1000 // 100] + tens[num % 100 // 10] + ones[num % 10])


if __name__ == '__main__':

    # Inputs
    num1 = 3
    num2 = 58
    num3 = 1994

    # Run tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()

    test_1 = solution_1.intToRoman(num1)
    test_2 = solution_2.intToRoman(num2)
    test_3 = solution_3.intToRoman(num3)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")
    print(f"Test 3: {test_3}")