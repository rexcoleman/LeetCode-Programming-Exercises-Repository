from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window
        # in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C.
        # Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals
            # to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1

            # Keep expanding the window once we are done contracting.
            r += 1

        return "" if ans[0] == float('inf') else s[ans[1]: ans[2] + 1]






if __name__ == '__main__':

    # Inputs and Expected Outputs
    s_1 = "ADOBECODEBANC"
    t_1 = "ABC"
    expected_output_1 = "BANC"
    s_2 = "a"
    t_2 = "a"
    expected_output_2 = "a"
    s_3 = "a"
    t_3 = "aa"
    expected_output_3 = ""

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.minWindow(s_1, t_1)
    test_2 = solution_2.minWindow(s_2, t_2)
    test_3 = solution_3.minWindow(s_3, t_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")