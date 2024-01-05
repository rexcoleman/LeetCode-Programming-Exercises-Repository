from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            # If we included a zero in the window we reduce the value of k.
            # Since k is the maximum zeros allowed in a window.
            k -= 1 - nums[right]
            # A negative k denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if k < 0:
                # If the left element to be thrown out is zero we increase k.
                k += 1 - nums[left]
                left += 1
        return right - left + 1


if __name__ == '__main__':

    # Inputs and Expected Outputs:
    nums_1 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k_1 = 2
    expected_output_1 = 6
    nums_2 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k_2 = 3
    expected_output_2 = 10

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.longestOnes(nums_1, k_1)
    test_2 = solution_2.longestOnes(nums_2, k_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")