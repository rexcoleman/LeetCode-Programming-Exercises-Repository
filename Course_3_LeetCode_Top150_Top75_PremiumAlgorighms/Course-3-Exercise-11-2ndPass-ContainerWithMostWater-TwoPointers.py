from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        max_water = 0
        while end > start:
            high = min(height[start], height[end])
            wide = end - start
            max_water = max(max_water, high * wide)
            if height[start] < height[end]:
                start += 1
            else: end -= 1

        return max_water

if __name__ == '__main__':

    # Inputs and Expected Outputs
    height_1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    expected_output_1 = 49
    height_2 = [1, 1]
    expected_output_2 = 1

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.maxArea(height_1)
    test_2 = solution_2.maxArea(height_2)

    # Prnt Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 1 Output: {test_2} \nExpected Output: {expected_output_2}")
