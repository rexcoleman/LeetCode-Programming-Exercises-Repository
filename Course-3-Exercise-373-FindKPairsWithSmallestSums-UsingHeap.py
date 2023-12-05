from typing import List
from heapq import heappop, heappush



class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)

        ans = []
        visited = set()

        minHeap = [(nums1[0] + nums2[0], (0, 0))]
        visited.add((0, 0))
        count = 0

        while k > 0 and minHeap:
            val, (i, j) = heappop(minHeap)
            ans.append([nums1[i], nums2[j]])

            if i + 1 < m and (i + 1, j) not in visited:
                heappush(minHeap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited:
                heappush(minHeap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))
            k = k - 1

        return ans





if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums1_1 = [1, 7, 11]
    nums2_1 = [2, 4, 6]
    k_1 = 3
    expected_output_1 = [[1, 2], [1, 4], [1, 6]]
    nums1_2 = [1, 1, 2]
    nums2_2 = [1, 2, 3]
    k_2 = 2
    expected_output_2 = [[1, 1], [1, 1]]
    nums1_3 = [1, 2]
    nums2_3 = [3]
    k_3 = 3
    expected_output_3 = [[1, 3], [2, 3]]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.kSmallestPairs(nums1_1, nums2_1, k_1)
    test_2 = solution_2.kSmallestPairs(nums1_2, nums2_2, k_2)
    test_3 = solution_3.kSmallestPairs(nums1_3, nums2_3, k_3)

    # Print Results
    print(f"\nTest 1 Result: {test_1} \nExpected Result: {expected_output_1}")
    print(f"\nTest 2 Result: {test_2} \nExpected Result: {expected_output_2}")
    print(f"\nTest 3 Result: {test_3} \nExpected Result: {expected_output_3}")
