from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque()
        r_count, d_count = 0, 0
        r_skip, d_skip = 0, 0
        res = ''

        for senator in senate:
            if senator == 'R':
                r_count += 1
            else:
                d_count += 1
            queue.append(senator)

        while queue:
            current = queue.popleft()
            if current == 'R':
                if r_skip > 0:
                    r_skip -= 1
                    r_count -= 1
                    continue
                if d_count == 0:
                    res = 'Radiant'
                    return res
                else:
                    d_skip += 1
                    queue.append(current)

            else:
                if d_skip > 0:
                    d_skip -= 1
                    d_count -= 1
                    continue
                if r_count == 0:
                    res = 'Dire'
                    return res
                else:
                    r_skip += 1
                    queue.append(current)


if __name__ == '__main__':

    # Inputs and Expected Outputs
    senate_1 = "RD"
    expected_output_1 = "Radiant"
    senate_2 = "RDD"
    expected_output_2 = "Dire"

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.predictPartyVictory(senate_1)
    test_2 = solution_2.predictPartyVictory(senate_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")