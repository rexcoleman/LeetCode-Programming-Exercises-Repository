from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize the counter and the second pointer
        j, count = 1, 1
        # Start from the second element in the array and process
        # the elements one by one
        for i in range(1, len(nums)):
            # If the current element is a duplicate,
            # increment the count
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                # Reset the count since we encountered a different
                # element from the previous one
                count = 1
            # for a count <= 2, we copy the element over thus
            # overwriting the element at index "j" in the array.
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j





if __name__ == '__main__':

    # Inputs
    nums1 = [1, 1, 1, 2, 2, 3]
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]

    test_1 = Solution()
    test_2 = Solution()

    t_1 = test_1.removeDuplicates(nums1)
    t_2 = test_2.removeDuplicates(nums2)

    print(f"Test 1: {t_1}")
    print(f"Test 2: {t_2}")