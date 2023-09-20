
# include all relavent roman numaral values in dictionary (hash table)
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}


class Solution(object):
    def romanToInt(self, s):
        # tracks the cumulative total
        total = 0
        # pointer to loop through s
        i = 0

        # iterate through string
        while i < len(s):
            # conditional for two character roman numerals
            if i < len(s) -1 and s[i:i+2] in values:
                total += values[s[i:i+2]]
                i += 2
            else:
                # conditional for single character roman numerals
                total += values[s[i]]
                i += 1
        return total





if __name__ == '__main__':
    solution = Solution()

    s1 = "III"
    s2 = "LVIII"
    s3 = "MCMXCIV"

    output1 = solution.romanToInt(s1)
    output2 = solution.romanToInt(s2)
    output3 = solution.romanToInt(s3)

    print(f"The value of s1 is: {output1}")
    print(f"The value of s2 is: {output2}")
    print(f"The value of s3 is: {output3}")