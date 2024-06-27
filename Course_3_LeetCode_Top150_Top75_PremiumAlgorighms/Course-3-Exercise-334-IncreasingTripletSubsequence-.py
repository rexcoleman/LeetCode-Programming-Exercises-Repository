from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = second_num = float('inf')
        len_nums = len(nums)
        for i in range(len_nums):
            if nums[i] <= first_num:
                first_num = nums[i]
            elif nums[i] <= second_num:
                second_num = nums[i]
            else:
                return True
        return False




if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [1, 2, 3, 4, 5]
    expected_output_1 = True
    nums_2 = [5,4,3,2,1]
    expected_output_2 = False
    nums_3 = [2, 1, 5, 0, 4, 6]
    expected_output_3 = True
    nums_4 = [0, 4, 2, 1, 0, -1, -3]
    expected_output_4 = False
    nums_5 = [20, 100, 10, 12, 5, 13]
    expected_output_5 = True

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    solution_5 = Solution()
    test_1 = solution_1.increasingTriplet(nums_1)
    test_2 = solution_2.increasingTriplet(nums_2)
    test_3 = solution_3.increasingTriplet(nums_3)
    test_4 = solution_4.increasingTriplet(nums_4)
    test_5 = solution_5.increasingTriplet(nums_5)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
    print(f"\nTest 4 Output: {test_4} \nExpected Output: {expected_output_4}")
    print(f"\nTest 5 Output: {test_5} \nExpected Output: {expected_output_5}")


