from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        node_group_info = {}

        def find(node_id):
            if node_id not in node_group_info:
                node_group_info[node_id] = (node_id, 1)
            group_id, node_multiplier = node_group_info[node_id]
            # The above statements are equivalent to the following one
            #group_id, node_multiplier = node_group_info.setdefault(node_id, (node_id, 1))

            if group_id != node_id:
                # found inconsistency, trigger chain update
                new_group_id, group_positional_multiplier =  find(group_id)
                node_group_info[node_id] = (new_group_id, node_multiplier * group_positional_multiplier)

            return node_group_info[node_id]

        def union(dividend, divisor, value):
            dividend_group_id, dividend_multiplier = find(dividend)
            divisor_group_id, divisor_multiplier = find(divisor)
            if dividend_group_id != divisor_group_id:
                # merge the two groups to gether,
                # by attaching the dividend group to the one of divisor
                node_group_info[dividend_group_id] = (divisor_group_id, divisor_multiplier * value / dividend_multiplier)

        # Step 1). build the union groups
        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)

        results = []
        # Step 2). run the evaluation, with "lazy" updates in find() function
        for (dividend, divisor) in queries:
            if dividend not in node_group_info or divisor not in node_group_info:
                # case 1). at least one variable did not appear before
                results.append(-1.0)
            else:
                dividend_group_id, dividend_multiplier = find(dividend)
                divisor_group_id, divisor_multiplier = find(divisor)
                if dividend_group_id != divisor_group_id:
                    # case 2). the variables do not belong to the same chain/group
                    results.append(-1.0)
                else:
                    # case 3). there is a chain/path between the variables
                    results.append(dividend_multiplier / divisor_multiplier)
        return results




if __name__ == '__main__':

    # Inputs and Expected Outputs
    equations_1 = [["a", "b"], ["b", "c"]]
    values_1 = [2.0, 3.0]
    queries_1 = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    expected_output_1 = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
    equations_2 = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values_2 = [1.5, 2.5, 5.0]
    queries_2 = [["a", "c"], ["c", "b"],["bc", "cd"], ["cd", "bc"]]
    expected_output_2 = [3.75000, 0.40000, 5.00000, 0.20000]
    equations_3 = [["a", "b"]]
    values_3 = [0.5]
    queries_3 = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    expected_output_3 = [0.50000, 2.00000, -1.00000, -1.00000]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    result_1 = solution_1.calcEquation(equations_1, values_1, queries_1)
    result_2 = solution_2.calcEquation(equations_2, values_2, queries_2)
    result_3 = solution_3.calcEquation(equations_3, values_3, queries_3)
    print(f"\nTest 1: {result_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2: {result_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3: {result_3} \nExpected Result: {expected_output_3}")
