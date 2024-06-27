from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        a = []
        a = set(nums1) - set(nums2)
        b = []
        b = set(nums2) - set(nums1)
        res.append(list(a))
        res.append(list(b))
        return res


if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums1_1 = [1, 2, 3]
    nums2_1 = [2, 4, 6]
    expected_output_1 = [[1, 3], [4, 6]]
    nums1_2 = [1, 2, 3, 3]
    nums2_2 = [1, 1, 2, 2]
    expected_output_2 = [[3], []]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.findDifference(nums1_1, nums2_1)
    test_2 = solution_2.findDifference(nums1_2, nums2_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")


