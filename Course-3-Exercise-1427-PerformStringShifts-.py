from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        len_s = len(s)
        net_shift = 0
        for direction, amount in shift:
            if direction == 0:
                net_shift -= amount
            else:
                net_shift += amount
        net_shift = net_shift % len_s
        return s[len_s - net_shift:] + s[:len_s - net_shift]


if __name__ == '__main__':

    # Inputs and Expected Outputs
    s_1 = "abc"
    shift_1 = [[0, 1], [1, 2]]
    expected_output_1 = "cab"
    s_2 = "abcdefg"
    shift_2 = [[1, 1], [1, 1], [0, 2], [1, 3]]
    expected_output_2 = "efgabcd"

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.stringShift(s_1, shift_1)
    test_2 = solution_2.stringShift(s_2, shift_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")