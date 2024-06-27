from collections import defaultdict


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        n = len(s)
        if k > 26:
            return 0
        answer = 0
        left = right = 0
        freq = [0] * 26

        # Function to obtain the index of a character according to the alphabet
        def get_val(ch: str) -> str:
            return ord(ch) - ord('a')

        while right < n:
            freq[get_val(s[right])] += 1

            while freq[get_val(s[right])] > 1:
                freq[get_val(s[left])] -= 1
                left += 1

            if right - left + 1 == k:
                answer += 1
                freq[get_val(s[left])] -= 1
                left += 1

            right += 1

        return answer


if __name__ == '__main__':

    # Inputs and Expected Outputs
    s_1 = "havefunonleetcode"
    k_1 = 5
    expected_output_1 = 6
    s_2 = "home"
    k_2 = 5
    expected_output_2 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.numKLenSubstrNoRepeats(s_1, k_1)
    test_2 = solution_2.numKLenSubstrNoRepeats(s_2, k_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
