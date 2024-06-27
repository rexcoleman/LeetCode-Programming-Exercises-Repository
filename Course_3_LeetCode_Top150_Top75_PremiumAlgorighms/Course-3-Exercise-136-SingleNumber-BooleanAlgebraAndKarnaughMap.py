from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Count (modulo 3) bits
        # msb (most significant bit), lsb (least significant bit)
        msb, lsb = 0, 0

        # Process Every Num and update count bits
        # ~msb : this is the NOT operator.  It reverses the bits in msb 0 -> 1 or 1 -> 0
        # Except it looks different in python due to Two's Complement.
        # & : this is the AND operator.  If both of the bits are 1 then the result is 1
        # otherwise it is 0
        for num in nums:
            a = (~msb & ~lsb & num)
            b = (lsb & ~num)
            new_lsb = (~msb & ~lsb & num) | (lsb & ~num)
            new_msb = (lsb & num) | (msb & ~num)
            lsb = new_lsb
            msb = new_msb

        # Return lsb as the answer
        return lsb


if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [2, 2, 3, 2]
    expected_output_1 = 3
    nums_2 = [0, 1, 0, 1, 0, 1, 99, 100, 100, 100]
    expected_output_2 = 99

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.singleNumber(nums_1)
    test_2 = solution_2.singleNumber(nums_2)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")