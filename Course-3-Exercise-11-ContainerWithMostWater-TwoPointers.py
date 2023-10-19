from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxarea



if __name__ == '__main__':
    # Inputs
    height1 = [1,8,6,2,5,4,8,3,7]
    height2 = [1,1]

    solution1 = Solution()
    solution2 = Solution()

    test_1 = solution1.maxArea(height1)
    test_2 = solution1.maxArea(height2)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")