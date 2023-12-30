from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        slow, fast = 0, 0
        length = len(chars)
        if length == 1:
            return 1
        while fast < length:
            if fast - slow == 10:
                slow += 1
                chars[slow] = 1
                slow += 1
                chars[slow] = 0
                while fast < length:
                    while chars[fast] == chars[slow + 1]:
                        chars[slow] += 1
                        fast += 1

            if chars[fast] != chars[slow]:
                diff = fast - slow
                if diff == 1:
                    slow += 1
                else:
                    chars[slow + 1] = diff
                    slow += 2
                    fast = slow
            else:
                fast += 1
        diff = fast - slow
        chars[slow + 1] = diff
        slow += 2
        while fast > slow:
            chars.pop()
            fast -= 1
        return len(chars)












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


