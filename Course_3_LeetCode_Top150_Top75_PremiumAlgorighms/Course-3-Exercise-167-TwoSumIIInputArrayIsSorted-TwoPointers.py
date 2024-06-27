from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1






if __name__ == '__main__':

    # Inputs
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    numbers2 = [2, 3, 4]
    target2 = 6
    numbers3 = [-1, 0]
    target3 = -1

    solution1 = Solution()
    solution2 = Solution()
    solution3 = Solution()

    test_1 = solution1.twoSum(numbers1, target1)
    test_2 = solution1.twoSum(numbers2, target2)
    test_3 = solution1.twoSum(numbers3, target3)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")
    print(f"Test 3: {test_3}")
