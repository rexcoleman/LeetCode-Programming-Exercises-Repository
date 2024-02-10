import heapq
from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        mapping = {}
        result = []
        for student_id, score in items:
            if student_id not in mapping:
                mapping[student_id] = []
            heapq.heappush(mapping[student_id], score)
            if len(mapping[student_id]) > 5:
                heapq.heappop(mapping[student_id])

        for student_id, scores in mapping.items():
            avg_score = sum(scores) // len(scores)
            result.append([student_id, avg_score])

            result.sort(key=lambda x: x[0])




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