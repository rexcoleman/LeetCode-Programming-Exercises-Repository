from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Length of input array
        length = len(nums)

        #Left and right arrays
        L, R, answer = [0] * length, [0] * length, [0] * length

        # L[i] contains the product of all the elements to the left
        # For the element at index '0,' there are no elements to the left
        # Set L[0] to 1
        L[0] = 1
        for i in range(1,length):
            # L[i - 1] already contains the product of elements to the
            # left of 'i - 1.'
            # Simply multiplying it with nums[i - 1] would give the product of
            # all elements to the left of index 'i.'
            L[i] = nums[i - 1] * L[i - 1]

        # R[i] contains the product of all elements to the right
        # For the element at index 'lenght - 1,' there are no elements to the right.
        # Set R[length - 1] to 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            # R[i + 1] already contains the product of the elements to the right of 'i + 1'
            # Multiplying it by nums[i + 1] would give the product of all elements
            # to the right of index i
            R[i] = nums[i + 1] * R[i + 1]

        # Constructing the answer array
        for i in range(length):
            # For the first element, R[i] would be the product except self
            # For the last element, L[i] would be the product except self
            # Else multiply the product of all elemetns to the left and to the right
            answer[i] = L[i] * R[i]

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