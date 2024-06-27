from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        ans = []
        backtrack([])
        return ans




if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [1,2,3]
    expected_output_1 = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    nums_2 = [0,1]
    expected_output_2 = [[0,1],[1,0]]
    nums_3 = [1]
    expected_output_3 = [[1]]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.permute(nums_1)
    test_2 = solution_2.permute(nums_2)
    test_3 = solution_3.permute(nums_3)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3 Result: {test_3} \nExpected Result: {expected_output_3}")
