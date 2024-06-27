from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Length of input array
        length = len(nums)

        # The answer array to be returned
        answer = [0] * length

        # answer[i] contains the product of all elements to the left
        # For the element at index '0,'there are no elements to the left
        # Therefore set answer[0] to 1
        answer[0] = 1
        for i in range(1, length):
            # answer[i - 1] already contains the product of the elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all elements to
            # the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]

        # R contains the product of all elements to the right
        # For the element at index 'length - 1,' there are no elements to the right
        # Therefore set R to 1
        R = 1
        for i in reversed(range(length)):
            # For the index 'i,' R contains the product of all elements to the right
            # Update R with each iteration
            answer[i] = answer[i] * R
            R *= nums[i]
        return answer






if __name__ == '__main__':

    # Inputs
    nums1 = [1, 2, 3, 4]
    nums2 = [-1, 1, 0, -3, 3]

    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.productExceptSelf(nums1)
    test_2 = solution_2.productExceptSelf(nums2)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")