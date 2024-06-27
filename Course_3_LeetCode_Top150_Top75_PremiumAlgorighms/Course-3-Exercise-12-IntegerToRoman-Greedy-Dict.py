class Solution:
    def intToRoman(self, num: int) -> str:
        digits = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        roman_digits = []

        for value in digits.keys():
            while num >= value:
                roman_digits.append(digits[value])
                num -= value

        return ''.join(roman_digits)


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