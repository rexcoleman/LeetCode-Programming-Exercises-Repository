from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        na, nb = len(nums1), len(nums2)
        n = na + nb

        def solve(k, a_start, a_end, b_start, b_end):
            # If the segment of on array is empty, it means we have passed all
            # its elements, just return the corresponding element in the other array.
            if a_start > a_end:
                return nums2[k - a_start]
            if b_start > b_end:
                return nums1[k - b_start]

            # Get the middle indexes and middle values of A and B.
            a_index, b_index = (a_start + a_end) // 2, (b_start + b_end) // 2
            a_value, b_value = nums1[a_index], nums2[b_index]

            # If k is in the right half of A + B, remove the smaller left half.
            if a_index + b_index < k:
                if a_value > b_value:
                    return solve(k, a_start, a_end, b_index + 1, b_end)
                else:
                    return solve(k, a_index + 1, a_end, b_start, b_end)
            # Otherwise, remove the larger right half.
            else:
                if a_value > b_value:
                    return solve(k, a_start, a_index - 1, b_start, b_end)
                else:
                    return solve(k, a_start, a_end, b_start, b_index - 1)

        if n % 2:
            return solve(n // 2, 0, na - 1, 0,  nb - 1)
        else:
            return (solve(n // 2 - 1, 0, na - 1, 0, nb - 1) +
                    solve(n // 2, 0, na - 1, 0, nb - 1)) / 2


if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums1_1 = [1, 3]
    nums2_1 = [2]
    expected_output_1 = 2.00000
    nums1_2 = [1, 2]
    nums2_2 = [3, 4]
    expected_output_2 = 2.50000

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.findMedianSortedArrays(nums1_1, nums2_1)
    test_2 = solution_2.findMedianSortedArrays(nums1_2, nums2_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1:.5f} \nExpected Output: {expected_output_1:.5f}")
    print(f"\nTest 2 Output: {test_2:.5f} \nExpected Output: {expected_output_2:.5f}")