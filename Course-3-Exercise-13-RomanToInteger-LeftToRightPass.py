
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
        # tracks the cumulative total
        total = 0
        # pointer to loop through s
        i = 0
        # O(1) running time because we are pulling from a hash table
        while i < len(s):

            # this condition identifes when we need to subtract a character \
            # from the following character and move the pointer 2 spaces
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1 ]]:
                total += values[s[i+1]] - values[s[i]]
                i += 2
                # print(total)
            # otherwise we add the value to the total and move forward 1 space
            else:
                total += values[s[i]]
                i += 1
                # print(total)
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