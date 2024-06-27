from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # The starting range of the first jump is [0, 0]
        answer, n = 0, len(nums)
        curr_end, curr_far = 0, 0

        for i in range(n - 1):
            # Update the furthest reachable index for this jump.
            curr_far = max(curr_far, i + nums[i])

            # If we finish the starting range of this jump,
            # move on to the starting range of the next jump.
            if i == curr_end:
                answer += 1
                curr_end = curr_far
        return answer

if __name__ == '__main__':

    # Inputs
    nums1 = [2,3,1,1,4]
    nums2 = [2,3,0,1,4]

    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.jump(nums1)
    test_2 = solution_2.jump(nums2)

    print(f"Maximum Jump 1: {test_1}")
    print(f"Maximum Jump 2: {test_2}")