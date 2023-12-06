from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize seen_once and seen_twice to 0
        seen_once = seen_twice = 0
        # Iterate through nums
        for num in nums:
            # Update using derived equations
            # seen_once ^ num : this is the XOR operator.  It makes seen_once the opposite of num 1 or 0
            # ~seen_twice : this is the NOT operator.  It reverses seen_twice 0 -> 1 or 1 -> 0
            # Except it looks different in python due to Two's Complement.
            # & : this is the AND operator.  If both of the above items are 1 then the result is 1
            # otherwise it is 0
            seen_once = (seen_once ^ num) & (~seen_twice)
            seen_twice = (seen_twice ^ num) & (~seen_once)

        # Return integer which appears exactly once
        return seen_once


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