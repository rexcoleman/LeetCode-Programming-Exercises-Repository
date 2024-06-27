from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Loner
        loner = 0

        # Iterate over all bits
        for shift in range(32):
            bit_sum = 0
            # For this bit, iterate over all integers
            for num in nums:
                # Compute the bit of num and add it to bit_sum
                a = num >> shift
                bin_a = bin(a)
                bit_sum += (num >> shift) & 1
                bin_bit_sum = bin(bit_sum)

            # Compute the bit of loner and place it
            loner_bit = bit_sum % 3
            b = loner_bit << shift
            bin_b = bin(b)
            loner = loner | (loner_bit << shift)

        # Do not mistake sign bit for MSB
        if loner >= (1 << 31):
            loner = loner - (1 << 32)

        return loner



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