class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(needle)
        n = len(haystack)
        if n < m:
            return -1

        # CONSTANTS
        RADIX = 26
        MOD = 1_000_000_033
        MAX_WEIGHT = 1

        # hashes for the region of needle and the haystack
        hash_haystack = 0
        hash_needle = 0



        # the largest polynomial term in the fingerprint function
        for _ in range(m - 1):
            MAX_WEIGHT = (MAX_WEIGHT * RADIX) % MOD

        # pre-compute the hash of the haystack in O(M)
        for i in range(m):
            hash_haystack = (RADIX * hash_haystack + ord(haystack[i])) % MOD
            hash_needle = (RADIX * hash_needle + ord(needle[i])) % MOD

        # slide the pattern over the text one by one
        for i in range (n - m + 1):

            # check the hash values of the current window of haystack
            # and needle. If the hash values match then only
            # check for characters one by one
            if hash_haystack == hash_needle:
                # naive approach to check the characters
                j = 0
                while j <= m:
                    if haystack[i + j] != needle[j]:
                        break
                    j += 1

                    if j == m:
                        return(i)


            # update the hash for the actual substring of the text
            # apply the rolling hash approach
            if i < n - m:
                hash_haystack = ((hash_haystack - ord(haystack[i]) * MAX_WEIGHT) * RADIX + ord(haystack[i + m])) % MOD

                # we might get a negative value so we have to make sure the hash is positive
                if hash_haystack < 0:
                    hash_haystack += MOD
            else:
                return -1




if __name__ == '__main__':

    haystack1 = "sadbutsad"
    needle1 = "sad"
    haystack2 = "leetcode"
    needle2 = "leeto"
    haystack3 = "mississippi"
    needle3 = "a"
    haystack4 = "a"
    needle4 = "a"
    haystack5 = "abc"
    needle5 = "c"

    solution = Solution()

    output1 = solution.strStr(haystack1, needle1)
    output2 = solution.strStr(haystack2, needle2)
    output3 = solution.strStr(haystack3, needle3)
    output4 = solution.strStr(haystack4, needle4)
    output5 = solution.strStr(haystack5, needle5)

    print(f"Output1: {output1}")
    print(f"Output2: {output2}")
    print(f"Output3: {output3}")
    print(f"Output4: {output4}")
    print(f"Output5: {output5}")


