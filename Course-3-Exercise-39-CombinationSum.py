from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()


        backtrack(target, [], 0)

        return results




if __name__ == '__main__':

    # Inputs and Expected Outputs
    candidates_1 = [2,3,6,7]
    target_1 = 7
    expected_output_1 = [[2,2,3],[7]]
    candidates_2 = [2,3,5]
    target_2 = 8
    expected_output_2 = [[2,2,2,2],[2,3,3],[3,5]]
    candidates_3 = [2]
    target_3 = 1
    expected_output_3 = []

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.combinationSum(candidates_1, target_1)
    test_2 = solution_2.combinationSum(candidates_2, target_2)
    test_3 = solution_3.combinationSum(candidates_3, target_3)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3 Result: {test_3} \nExpected Result: {expected_output_3}")
