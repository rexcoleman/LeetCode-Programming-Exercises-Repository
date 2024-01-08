from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        def decode(encoded, current_position):
            decoded_substring = ""
            index, repeat_count = current_position, 0
            while index < len(encoded):
                digit_value = ord(encoded[index]) - 48  # ASCII value of '0' is 48
                if 0 <= digit_value <= 9:  # Check if it's a digit
                    repeat_count = repeat_count * 10 + digit_value
                elif encoded[index] == '[':
                    nested_string, next_position = decode(encoded, index + 1)
                    decoded_substring += nested_string * repeat_count
                    index = next_position
                    repeat_count = 0
                elif encoded[index] == ']':
                    return decoded_substring, index
                else:
                    decoded_substring += encoded[index]
                index += 1
            return decoded_substring, index

        return decode(s, 0)[0]


if __name__ == '__main__':
    # Inputs and Expected Outputs:
    s_1 = "3[a]2[bc]"
    expected_output_1 = "aaabcbc"
    s_2 = "3[a2[c]]"
    expected_output_2 = "accaccacc"
    s_3 = "2[abc]3[cd]ef"
    expected_output_3 = "abcabccdcdcdef"

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.decodeString(s_1)
    test_2 = solution_2.decodeString(s_2)
    test_3 = solution_3.decodeString(s_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
