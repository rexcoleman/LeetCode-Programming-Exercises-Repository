from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        p1, p2 = 0, 0

        # Get the smaller value between nums1[p1] and nums2[p2].
        def get_min():
            nonlocal p1, p2
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p2 == n:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
            return ans

        if (m + n) % 2 == 0:
            for _ in range(((m + n) // 2) - 1):
                _ = get_min()
            return float((get_min() + get_min()) / 2)
        else:
            for _ in range((m + n) // 2):
                _ = get_min()
            return float(get_min())


if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums1_1 = [1, 3]
    nums2_1 = [2]
    expected_output_1 = 2.00000
    nums1_2 = [3, 4, 5, 6]
    nums2_2 = [4, 5, 6, 7]
    expected_output_2 = 5.00000

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.findMedianSortedArrays(nums1_1, nums2_1)
    test_2 = solution_2.findMedianSortedArrays(nums1_2, nums2_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1:.5f} \nExpected Output: {expected_output_1:.5f}")
    print(f"\nTest 2 Output: {test_2:.5f} \nExpected Output: {expected_output_2:.5f}")