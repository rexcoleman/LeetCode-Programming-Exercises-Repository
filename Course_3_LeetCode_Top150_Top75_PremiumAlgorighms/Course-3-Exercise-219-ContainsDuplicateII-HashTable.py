class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index_dict = {}

        for i, n in enumerate(nums):
            if n in index_dict and i - index_dict[n] <= k:
                return True

            index_dict[n] = i

        return False




if __name__ == "__main__":

    solution = Solution()

    nums1 = [1,2,3,1]
    k1 = 3

    nums2 = [1,0,1,1]
    k2 = 1

    nums3 = [1,2,3,1,2,3]
    k3 = 2

    outcome1 = solution.containsNearbyDuplicate(nums1, k1)
    outcome2 = solution.containsNearbyDuplicate(nums2, k2)
    outcome3 = solution.containsNearbyDuplicate(nums3, k3)

    print(f"Outcome1: {outcome1}")
    print(f"Outcome2: {outcome2}")
    print(f"Outcome3: {outcome3}")