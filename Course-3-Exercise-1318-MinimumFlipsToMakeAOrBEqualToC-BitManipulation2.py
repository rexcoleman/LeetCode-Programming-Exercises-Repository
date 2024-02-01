class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            if c & 1:
                ans += 0 if ((a & 1) or (b & 1)) else 1
            else:
                ans += (a & 1) + (b & 1)
            a >>= 1
            b >>= 1
            c >>= 1

        return ans


if __name__ == '__main__':

    # Inputs and Expected Outputs
    a_1 = 2
    b_1 = 6
    c_1 = 5
    expected_output_1 = 3
    a_2 = 4
    b_2 = 2
    c_2 = 7
    expected_output_2 = 1
    a_3 = 1
    b_3 = 2
    c_3 = 3
    expected_output_3 = 0
    a_4 = 8
    b_4 = 3
    c_4 = 5
    expected_output_4 = 3

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    test_1 = solution_1.minFlips(a_1, b_1, c_1)
    test_2 = solution_2.minFlips(a_2, b_2, c_2)
    test_3 = solution_3.minFlips(a_3, b_3, c_3)
    test_4 = solution_4.minFlips(a_4, b_4, c_4)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
    print(f"\nTest 4 Output: {test_4} \nExpected Output: {expected_output_4}")

