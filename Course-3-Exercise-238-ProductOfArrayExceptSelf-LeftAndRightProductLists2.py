from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        # left product list
        left_product_list = [1] * len_nums
        right_product_list = [1] * len_nums
        output = []
        for i in range(1, len_nums):
            left_product_list[i] = left_product_list[i-1] * nums[i-1]
        for i in range(len_nums -2,-1,-1):
            right_product_list[i] = right_product_list[i+1] * nums[i+1]
        for i in range(len_nums):
            output.append(left_product_list[i] * right_product_list[i])
        return output







if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [1, 2, 3, 4]
    expected_output_1 = [24, 12, 8, 6]
    nums_2 = [-1, 1, 0, -3, 3]
    expected_output_2 = [0, 0, 9, 0, 0]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.productExceptSelf(nums_1)
    test_2 = solution_2.productExceptSelf(nums_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")



