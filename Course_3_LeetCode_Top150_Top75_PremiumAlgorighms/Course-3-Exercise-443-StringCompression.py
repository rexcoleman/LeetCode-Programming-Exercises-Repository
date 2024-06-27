from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            group_length = 1
            while i + group_length < len(chars) and chars[i + group_length] == chars[i]:
                group_length += 1
            chars[res] = chars[i]   # why?
            res += 1
            if group_length > 1:
                str_repr = str(group_length)
                a = list(str_repr)
                chars[res:res+len(str_repr)] = list(str_repr)
                res += len(str_repr)
            i += group_length
        return res


if __name__ == '__main__':

    # Inputs and Expected Outputs
    chars_1 = ["a","a","b","b","c","c","c"]
    expected_output_1 = 6
    chars_2 = ["a"]
    expected_output_2 = 1
    chars_3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    expected_output_3 = 4

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.compress(chars_1)
    test_2 = solution_2.compress(chars_2)
    test_3 = solution_3.compress(chars_3)

    # Prnt Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")


