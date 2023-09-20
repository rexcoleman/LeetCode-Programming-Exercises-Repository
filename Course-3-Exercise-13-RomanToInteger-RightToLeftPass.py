values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "M": 1000,
}

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # track the cumulative total
        total = 0
        i = 0

        # start with the last roman character's value in total
        total = values.get(s[-1])
        # create for look to iterate through string from right to left
        # commented out an alternative way to code the for loop
        # for i in reversed(range(len(s) - 1)):
        for i in range(len(s) - 2, -1, -1):
            # conditional for substraction case
            if values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                # conditional for addition case
                total += values[s[i]]
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