from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        mapping = {}
        result = []
        for x in items:
            if x[0] in mapping:
                mapping[x[0]].append(x[1])
            else:
                mapping[x[0]] = [x[1]]

        for x, y in mapping.items():
            y.sort(reverse=True)
            total = 0
            i = 0
            while i < 5 and i < len(y):
                total += y[i]
                i += 1
            result.append([x, total//i])
        return result



if __name__ == '__main__':

    # Inputs and Expected Outputs
    items_1 = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
    expected_output_1 = [[1, 87], [2, 88]]
    items_2 = [[1, 100], [7, 100], [1, 100], [7, 100], [1, 100], [7, 100], [1, 100], [7, 100], [1, 100], [7, 100]]
    expected_output_2 = [[1, 100], [7, 100]]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.highFive(items_1)
    test_2 = solution_2.highFive(items_2)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")