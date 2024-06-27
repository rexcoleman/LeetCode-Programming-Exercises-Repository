from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()


if __name__ == '__main__':

    # Inputs
    nums1 = [2, 2, 1]
    expected_output_1 = 1
    nums2 = [4, 1, 2, 1, 2]
    expected_output_2 = 4
    nums3 = [1]
    expected_output_3 = 1

    # Run Tests
    solution1 = Solution()
    solution2 = Solution()
    solution3 = Solution()
    test_1 = solution1.singleNumber(nums1)
    test_2 = solution2.singleNumber(nums2)
    test_3 = solution3.singleNumber(nums3)

    # Prnt Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")




