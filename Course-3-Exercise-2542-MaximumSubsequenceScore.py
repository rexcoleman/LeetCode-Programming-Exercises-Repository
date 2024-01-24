import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Sort pair (nums1[i], nums2[i]) by nums2[i] in decreasing order.
        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        # pairs.sort(key = lambda x: -x[1])
        pairs.sort(key=lambda x: -x[1])
        # Use a min-heap to maintain the top k elements.
        top_k_heap = [x[0] for x in pairs[:k]]
        top_k_sum = sum(top_k_heap)
        heapq.heapify(top_k_heap)

        # The score of the first k pairs.
        answer = top_k_sum * pairs[k - 1][1]

        # Iterate over every nums2[i] as minimum from nums2.
        for i in range(k, len(nums1)):
            # Remove the smallest integer from the previous top k elements
            # then add nums1[i] to the top k elements.
            top_k_sum -= heapq.heappop(top_k_heap)
            top_k_sum += pairs[i][0]
            heapq.heappush(top_k_heap, pairs[i][0])

            # Update answer as the maximum score.
            answer = max(answer, top_k_sum * pairs[i][1])

        return answer


if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums1_1 = [1, 3, 3, 2]
    nums2_1 = [2, 1, 3, 4]
    k_1 = 3
    expected_output_1 = 12
    nums1_2 = [4, 2, 3, 1, 1]
    nums2_2 = [7, 5, 10, 9, 6]
    k_2 = 1
    expected_output_2 = 30

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.maxScore(nums1_1, nums2_1, k_1)
    test_2 = solution_2.maxScore(nums1_2, nums2_2, k_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")