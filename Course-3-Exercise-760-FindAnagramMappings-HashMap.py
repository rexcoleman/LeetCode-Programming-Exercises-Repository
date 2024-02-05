from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        val_map = {val: i for i, val in enumerate(nums2)}
        output = [val_map[num] for num in nums1]

        return output


if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums1_1 = [12, 28, 46, 32, 50]
    nums2_1 = [50, 12, 32, 46, 28]
    expected_output_1 = [1, 4, 3, 2, 0]
    nums1_2 = [84, 46]
    nums2_2 = [84, 46]
    expected_output_2 = [0, 1]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.anagramMappings(nums1_1, nums2_1)
    test_2 = solution_2.anagramMappings(nums1_2, nums2_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")