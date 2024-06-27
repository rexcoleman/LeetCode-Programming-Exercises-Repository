from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        len_nums = len(nums)
        start, end = 0, len_nums - 1
        count = 0
        while nums[end] == 0 and start < end:
            end -= 1
            count += 1

        while start < len_nums - count:
            if nums[start] == 0:
                temp = nums[start]
                for i in range(start, len_nums - 1):
                    nums[i] = nums[i+1]
                nums[end] = temp
                count += 1
                continue
            start += 1


if __name__ == '__main__':

    # Inputs and Expected Outputs:
    nums_1 = [0, 1, 0, 3, 12]
    expected_output_1 = [1, 3, 12, 0, 0]
    nums_2 = [0]
    expected_output_2 = [0]
    nums_3 = [0,0,1]
    expected_output_3 = [1, 0, 0]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.moveZeroes(nums_1)
    test_2 = solution_2.moveZeroes(nums_2)
    test_3 = solution_3.moveZeroes(nums_3)

    # Print Results
    print(f"\nTest 1 Output: {nums_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {nums_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {nums_3} \nExpected Output: {expected_output_3}")