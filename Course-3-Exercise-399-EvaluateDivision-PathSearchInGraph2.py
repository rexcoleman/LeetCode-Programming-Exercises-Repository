from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(defaultdict)

        def backtrack_evaluate(curr_node, target_node, acc_product, visited):
            visited.add(curr_node)
            ret = -1.0
            neighbors = graph[curr_node]
            if target_node in neighbors:
                ret = acc_product * neighbors[target_node]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = backtrack_evaluate(neighbor, target_node, acc_product * value, visited)
                    if ret != -1.0:
                        break
            visited.remove(curr_node)
            return ret


        # Step 1). build the graph from the equations
        for (dividend, divisor), value in zip(equations, values):
            # add nodes and two edges into the graph
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        # Step 2). Evaluate each query via backtracking (DFS)
        #  by verifying if there exists a path from dividend to divisor
        results = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                # case 1): either node does not exist
                ret = -1.0
            elif dividend == divisor:
                # case 2): origin and destination are the same node
                ret = 1.0
            else:
                visited = set()
                ret = backtrack_evaluate(dividend, divisor, 1, visited)
            results.append(ret)

        return results


if __name__ == '__main__':

    # Inputs and Expected Outputs
    equations_1 = [["a", "b"], ["b", "c"]]
    values_1 = [2.0, 3.0]
    queries_1 = [["a", "c"], ["b", "a"], ["a", "e"],["a", "a"], ["x", "x"]]
    expected_output_1 = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
    equations_2 = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values_2 = [1.5, 2.5, 5.0]
    queries_2 = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    expected_output_2 = [3.75000, 0.40000, 5.00000, 0.20000]
    equations_3 = [["a", "b"]]
    values_3 = [0.5]
    queries_3 = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    expected_output_3 = [0.50000,2.00000,-1.00000,-1.00000]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.calcEquation(equations_1, values_1, queries_1)
    test_2 = solution_2.calcEquation(equations_2, values_2, queries_2)
    test_3 = solution_3.calcEquation(equations_3, values_3, queries_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")