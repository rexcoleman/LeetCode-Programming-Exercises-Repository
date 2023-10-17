from typing import List

class Solution:
    def hIndes(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        if len(citations) == 1 and citations[0] > 0:
            return 1
        if citations[-1] >= len(citations):
            return len(citations)
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i
        return 0



if __name__ == '__main__':

    # Inputs
    citations1 = [3, 0, 6, 1, 5]
    citations2 = [1, 3, 1]

    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.hIndes(citations1)
    test_2 = solution_2.hIndes(citations2)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")