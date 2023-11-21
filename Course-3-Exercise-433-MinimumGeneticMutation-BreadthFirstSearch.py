from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([(startGene, 0)])
        # A set can be initialized by {startGene} or set(startGene)
        # To convert a list to a set, use set(bank)
        bank = set(bank)
        seen = {startGene}
        print(type(seen))
        while queue:
            node, steps = queue.popleft()
            if node == endGene:
                return steps

            for mutation in "ACGT":
                for i in range(len(node)):
                    neighbor = node[:i] + mutation + node[i + 1:]
                    if neighbor not in seen and neighbor in bank:
                        queue.append((neighbor, steps + 1))
                        seen.add(neighbor)
        return -1



if __name__ == '__main__':

    # Inputs and Expected Outputs
    startGene_1 = "AACCGGTT"
    endGene_1 = "AACCGGTA"
    bank_1 = ["AACCGGTA"]
    expected_output_1 = 1
    startGene_2 = "AACCGGTT"
    endGene_2 = "AAACGGTA"
    bank_2 = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    expected_output_2 = 2

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.minMutation(startGene_1, endGene_1, bank_1)
    test_2 = solution_2.minMutation(startGene_2, endGene_2, bank_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
