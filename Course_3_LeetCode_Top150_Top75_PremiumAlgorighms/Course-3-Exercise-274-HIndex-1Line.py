from typing import List

class Solution:
    def hIndes(self, citations: List[int]) -> int:
        j = enumerate(sorted(citations, reverse=True))
        for index, value in j:
            print(f"Index: {index}, Value: {value}")
        k = [i < j for i, j in enumerate(sorted(citations, reverse=True))]
        print(k)


        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))



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