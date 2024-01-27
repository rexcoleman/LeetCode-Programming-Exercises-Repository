from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        results = []
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                # Otherwise the combination would be reverted in other branch of backtracking.
                # make a copy of current combination
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                # exceed the scope, no need to explore further.
                return

            # Iterate through the reduced list of candidates.
            for i in range(next_start, 9):
                comb.append(i + 1)
                backtrack(remain-i-1, comb, i+1)
                # backtrack the current choice
                comb.pop()

        backtrack(n, [], 0)

        return results


if __name__ == "__main__":

    # Inputs and Expected Outputs
    k_1 = 3
    n_1 = 7
    expected_output_1 = [[1, 2, 4]]
    k_2 = 3
    n_2 = 9
    expected_output_2 = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    k_3 = 4
    n_3 = 1
    expected_output_3 = []

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.combinationSum3(k_1, n_1)
    test_2 = solution_2.combinationSum3(k_2, n_2)
    test_3 = solution_3.combinationSum3(k_3, n_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")