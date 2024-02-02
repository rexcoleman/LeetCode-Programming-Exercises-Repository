from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for cur_day, cur_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur_temp:
                prev_day = stack.pop()
                answer[prev_day] = cur_day - prev_day
            stack.append(cur_day)

        return answer


if __name__ == '__main__':

    # Inputs and Expected Outputs
    temperatures_1 = [73, 74, 75, 71, 69, 72, 76, 73]
    expected_output_1 = [1, 1, 4, 2, 1, 1, 0, 0]
    temperatures_2 = [30, 40, 50, 60]
    expected_output_2 = [1, 1, 1, 0]
    temperatures_3 = [30, 60, 90]
    expected_output_3 = [1, 1, 0]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.dailyTemperatures(temperatures_1)
    test_2 = solution_2.dailyTemperatures(temperatures_2)
    test_3 = solution_3.dailyTemperatures(temperatures_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")