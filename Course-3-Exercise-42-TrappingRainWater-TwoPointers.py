from typing import List


class Solution:

    def sumBrackets(self, height: List[int], left, right):
        minHeightLeft = height[left]
        total = 0
        leftBracket = 0
        locationMinLeft = left

        while left < right:
            if height[left] < minHeightLeft:
                leftBracket += minHeightLeft - height[left]
            else:
                minHeightLeft = height[left]
                total += leftBracket
                leftBracket = 0
                locationMinLeft = left
            left += 1

        if minHeightLeft <= height[right]:
            return total + leftBracket, right
        else:
            return total, locationMinLeft

    def sumBracketsReverse(self, height: List[int], left, right):
        minHeightRight = height[right]
        total = 0
        rightBracket = 0
        locationMinRight = right

        while left < right:

            if height[right] < minHeightRight:
                rightBracket += minHeightRight - height[right]
            else:
                minHeightRight = height[right]
                total += rightBracket
                rightBracket = 0
                locationMinRight = right
            right -= 1

        if minHeightRight <= height[left]:
            return total + rightBracket, left

        else:
            return total, locationMinRight


    def trap(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0
        totalSum = 0

        while left < right - 1:
            if height[left] < height[right]:
                total, left = self.sumBrackets(height, left, right)
            else:
                total, right = self.sumBracketsReverse(height, left, right)

            totalSum += total

        return totalSum


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