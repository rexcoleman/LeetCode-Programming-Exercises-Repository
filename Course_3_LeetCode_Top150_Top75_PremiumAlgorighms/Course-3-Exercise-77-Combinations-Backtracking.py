from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr, first_num):
            if len(curr) == k:
                answer.append(curr[:])
                return

            # Need can be visually represented by layers of a tree with k layers
            need = k - len(curr)
            remain = n - first_num + 1
            # I struggled with conceptually grasping available.
            # We need to make sure we have enough nodes remaining (remain) to fill the need (need)
            # If we do not have enough nodes remaining then we do not need to calculate additional branches
            available = remain - need

            # +1 is used because the range() method is non-inclusive.
            for num in range(first_num, first_num + available + 1):
                curr.append(num)
                backtrack(curr, num + 1)
                curr.pop()
            return

        answer = []
        backtrack([], 1)
        return answer


if __name__ == '__main__':

    # Inputs and Expected Outputs
    n_1 = 4
    k_1 = 2
    expected_output_1 = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    n_2 = 1
    k_2 = 1
    expected_output_2 = [[1]]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.combine(n_1, k_1)
    test_2 = solution_2.combine(n_2, k_2)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
