from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        curr_flowers = sum(flowerbed)
        len_fb = len(flowerbed)
        if len_fb % 2:
            max_flowers = len_fb // 2 + 1
        else:
            max_flowers = len_fb // 2
        if curr_flowers + n > max_flowers:
            return False


        for i in range(len_fb):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i-1] == 0)
                empty_right_plot = (i == len_fb - 1) or (flowerbed[i + 1] == 0)

                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_plot:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return count >= n


if __name__ == '__main__':

    # Inputs and Expected Outputs
    flowerbed_1 = [1, 0, 0, 0, 1]
    n_1 = 1
    expected_output_1 = True
    flowerbed_2 = [1, 0, 0, 0, 1]
    n_2 = 2
    expected_output_2 = False
    flowerbed_3 = [1,0,1,0,1,0,1]
    n_3 = 0
    expected_output_3 = True
    flowerbed_4 = [0,0,1,0,1]
    n_4 = 1
    expected_output_4 = True
    flowerbed_5 = [1,0,0,0,1,0,0]
    n_5 = 2
    expected_output_5 = True

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    solution_5 = Solution()
    test_1 = solution_1.canPlaceFlowers(flowerbed_1, n_1)
    test_2 = solution_2.canPlaceFlowers(flowerbed_2, n_2)
    test_3 = solution_3.canPlaceFlowers(flowerbed_3, n_3)
    test_4 = solution_4.canPlaceFlowers(flowerbed_4, n_4)
    test_5 = solution_5.canPlaceFlowers(flowerbed_5, n_5)

    # Print to Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
    print(f"\nTest 4 Output: {test_4} \nExpected Output: {expected_output_4}")
    print(f"\nTest 5 Output: {test_5} \nExpected Output: {expected_output_5}")