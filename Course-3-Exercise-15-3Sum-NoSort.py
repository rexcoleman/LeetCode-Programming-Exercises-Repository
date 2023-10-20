from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result, duplicates = set(), set()
        seen = {}
        for i, value_1 in enumerate(nums):
            if value_1 not in duplicates:
                duplicates.add(value_1)
                for j, value_2 in enumerate(nums[i + 1:]):
                    complement = -value_1 - value_2
                    if complement in seen and seen[complement] == i:
                        result.add(tuple(sorted((value_1, value_2, complement))))
                    seen[value_2] = i
        return result


if __name__ == '__main__':
    # Inputs
    nums1 = [-1, 0, 1, 2, -1, -4]
    nums2 = [0, 1, 1]
    nums3 = [0, 0, 0]

    solution1 = Solution()
    solution2 = Solution()
    solution3 = Solution()

    test_1 = solution1.threeSum(nums1)
    test_2 = solution1.threeSum(nums2)
    test_3 = solution1.threeSum(nums3)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")
    print(f"Test 3: {test_3}")

