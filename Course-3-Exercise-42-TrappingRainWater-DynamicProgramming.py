from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return 0

        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        ##print(max_left, height)
        max_left[0] = 0
        max_right[n - 1] = 0
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i - 1])

        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])

        output = 0
        print(max_left, max_right)

        for i in range(n):
            lower_boundary = min(max_left[i], max_right[i])
            max_trap_at_i = lower_boundary - height[i]

            if max_trap_at_i > 0:
                output += max_trap_at_i

        return output


if __name__ == '__main__':

    # Inputs and Expected Outputs
    height_1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    expected_output_1 = 6
    height_2 = [4, 2, 0, 3, 2, 5]
    expected_output_2 = 9

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.trap(height_1)
    test_2 = solution_2.trap(height_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")