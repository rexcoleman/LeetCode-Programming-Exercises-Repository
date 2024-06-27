from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partitionA = (left + right) // 2
            partitionB = (m + n + 1) // 2 - partitionA

            maxLeftA = float('-inf') if partitionA == 0 else nums1[partitionA - 1]
            minRightA = float('inf') if partitionA == m else nums1[partitionA]
            maxLeftB = float('-inf') if partitionB == 0 else nums2[partitionB - 1]
            minRightB = float('inf') if partitionB == n else nums2[partitionB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                right = partitionA - 1
            else:
                left = partitionA + 1


if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums1_1 = [1, 3]
    nums2_1 = [2]
    expected_output_1 = 2.00000
    nums1_2 = [8, 9]
    nums2_2 = [1, 2, 3, 4, 5, 6, 7]
    expected_output_2 = 5.00000

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.findMedianSortedArrays(nums1_1, nums2_1)
    test_2 = solution_2.findMedianSortedArrays(nums1_2, nums2_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1:.5f} \nExpected Output: {expected_output_1:.5f}")
    print(f"\nTest 2 Output: {test_2:.5f} \nExpected Output: {expected_output_2:.5f}")