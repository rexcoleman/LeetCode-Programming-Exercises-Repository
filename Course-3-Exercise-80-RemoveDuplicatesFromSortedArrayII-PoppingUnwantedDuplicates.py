from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize the counter and array index
        i, count = 1, 1
        # Start from the second element in the array and process
        # elements one by one
        while i < len(nums):
            # If the current element is a duplicate,
            # increment the count
            if nums[i] == nums[i - 1]:
                count += 1
                # If the count is more than two, this is an unwanted
                # duplicate element.
                # We remove it from the array.
                if count > 2:
                    nums.pop(i)
                    # Note that we have to decrement the array
                    # index to keep it consistent with the
                    # size of the array.
                    i -= 1
            else:
                # Reset the count since we encountered a different
                # element from the previous one.
                count = 1
            # Move on to the next element in the array
            i += 1
        return len(nums)






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